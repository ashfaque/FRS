import os
from django.conf import settings

def get_directory_path(instance, filename):
    file_extension = os.path.splitext(filename)
    if file_extension[1] in ['.jpg', '.png', '.jpeg']:
        dir = 'images'
    elif file_extension[1] in ['.csv', '.pdf', '.doc', '.docx', '.xlsx', '.xls']:
        dir = 'documents'
    elif file_extension[1] in ['.mp4']:
        dir = 'videos'
    else:
        dir = "others"
    app_name = instance._meta.app_label
    model_name = instance._meta.object_name

    # Fetching current user Roll Number:-
    from users.models import UserDetail
    user_roll_no_obj = UserDetail.objects.filter(id=instance.id).order_by('id').last()
    user_roll_no = user_roll_no_obj.roll_no

    path = '{0}/{1}/{2}/{3}/{4}'.format(app_name, model_name, dir, user_roll_no, filename)
    return path


def save_face_data_while_creating_user(pk, instance, action='create', remarks=''):
    # ! Apply FRS here and save the string data somewhere in DB.
    # ? https://www.mygreatlearning.com/blog/face-recognition/
    from users.models import UserDetail
    # UserActionLog.objects.create(user=user, action=action, table_name=table_name, entity_id=entity_id, remarks=remarks)
    profile_image_dict = UserDetail.objects.filter(id = pk).values("profile_img", "roll_no").last()
    if profile_image_dict['profile_img']:
        
        print("###############  APPLY FRS HERE, FRS ENCODING DATA SAVED IN MEDIA DIR WITH ROLL NUMBER WISE IN EACH FILE  ########################----->", profile_image_dict['profile_img'])
        
        from imutils import paths
        import face_recognition
        import pickle
        import cv2
        import os
        
        #get paths of each file in folder named Images
        #Images here contains my data(folders of various persons)
        user_image_dir_path = '/'.join(profile_image_dict['profile_img'].split('/')[0:4])
        imagePaths = list(paths.list_images(os.path.join(settings.MEDIA_ROOT, user_image_dir_path)))
        knownEncodings = []
        knownRollNo = []
        # loop over the image paths
        for (i, imagePath) in enumerate(imagePaths):
            # extract the person name from the image path
            name = (imagePath.split(os.path.sep)[-2]).split('/')[-1]
            # load the input image and convert it from BGR (OpenCV ordering)
            # to dlib ordering (RGB)
            image = cv2.imread(imagePath)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            #Use Face_recognition to locate faces
            boxes = face_recognition.face_locations(rgb,model='hog')
            # compute the facial embedding for the face
            encodings = face_recognition.face_encodings(rgb, boxes)
            # loop over the encodings
            for encoding in encodings:
                knownEncodings.append(encoding)
                knownRollNo.append(name)
        #save encodings along with their names in dictionary data
        data = {"encodings": knownEncodings, "names": knownRollNo}
        #use pickle to save data into a file for later use
        face_encoding_dir_path = os.path.join(settings.MEDIA_ROOT, "face_encoding_data")
        if not os.path.exists(face_encoding_dir_path):
            os.makedirs(face_encoding_dir_path)
        f = open(os.path.join(face_encoding_dir_path, profile_image_dict['roll_no']), "wb")
        f.write(pickle.dumps(data))
        f.close()
