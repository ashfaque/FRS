from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
from pdb import set_trace as bp
import os
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.conf import settings
from rest_framework.exceptions import APIException
from django.db import transaction
from users.models import UserDetail
from .models import Attendance

import face_recognition
import imutils
import pickle
import time
import cv2
import os
import logging


log = logging.getLogger(__name__)
# log.info('text',variable)      # Usage


# ? Api to take forms data along with 5 images and apply frs on it and save it in db using student id as fkey and 5 images data in mapping table.
# ! img -> save -> frs on saved imgs -> db save hash code
# ! image -> frs -> db match -> roll no fetch
# * https://github.com/venugopalkadamba/Face_Verification_based_Attendance_system
# ? http://192.168.0.100:8888/, heidisql, postman, POST {{url}}users/login/ -> Header-> X-CSRFToken = {{mycsrftoken}}, Test = pm.globals.set("mycsrftoken", postman.getResponseCookie("csrftoken").value); , body email & password.
# ? WEBRTC r&d

@api_view(('POST',))
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def FMApplyFRSView(request):
    if request.method == 'POST':
        # image=request.POST.get("image", None)
        image_in_base64 = request.POST.get('image-base64', None)
        # log.info('image------------------------->',image_in_base64)
        # print("image------------>",image_in_base64)
        
        # ? https://www.codegrepper.com/code-examples/python/python+convert+base64+to+image

        # import re
        # image_in_base64 = re.sub("/[data:image\/[a-z]*;[a-z0-9]*,.*]/gm", "", image_in_base64)    # Removing : `data:image/jpeg;base64,`
        # print("-----",image_in_base64[:22])

        if image_in_base64:
            if os.path.exists(settings.FRS_MEDIA_ROOT + "captured.jpg"):
                # print(settings.FRS_MEDIA_ROOT + "captured.jpg")
                os.remove(settings.FRS_MEDIA_ROOT + "captured.jpg")

        import io, base64
        from PIL import Image
        # img = Image.open(io.BytesIO(base64.decodebytes(bytes(image_in_base64, "utf-8"))))
        img = Image.open(io.BytesIO(base64.decodebytes(bytes(image_in_base64[22:], "utf-8"))))
        rgb_im = img.convert('RGB')
        rgb_im.save(f"{settings.FRS_MEDIA_ROOT}captured.jpg")
        # img.save(f"{settings.FRS_MEDIA_ROOT}captured.png")

        # image_in_base64 = image_in_base64.encode('utf-8')
        # image_64_decode = base64.decodebytes(image_in_base64)
        
        
        
        # with open(f"{settings.FRS_MEDIA_ROOT}captured.jpg", 'wb+') as image_result:
            # image_result.write(image_64_decode)

        # print("image------------>",image)
        # log.info('text-------------->',str(image))      # Usage
            


        # ? from PIL import Image
        # ? image_object = Image.open(blob)

        # image=request.FILES['canvasImage.jpg']
        # image=request.POST.get
        # image = request.body['image']
        # image = request.FILES.get('image_data', None)
        # print("image------------>",image)
    # if image:
        # print("image------------>",image)
    # else: print("image not received----------------")
    # raise APIException("ksdfsjkfj")






    # if request.method == 'POST':
        # image = request.FILES.get('image', None)

        # img_extension = os.path.splitext(image.name)[-1]

# ! SAVE IMG taken from camera

        

        captured_image_full_path = os.path.join(settings.FRS_MEDIA_ROOT, "captured.jpg")
        # img_extension = '.' + image.split('.')[-1]
        
        



        # img_path = default_storage.save(settings.FRS_MEDIA_ROOT + "captured" + img_extension, image)
        # captured_image_full_path = os.path.join(settings.FRS_MEDIA_ROOT, f"captured{img_extension}")

        #find path of xml file containing haarcascade file
        cascPathface = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
        # load the harcaascade in the cascade classifier
        faceCascade = cv2.CascadeClassifier(cascPathface)
        # load the known faces and embeddings saved in last file

        face_encoding_dir_path = os.path.join(settings.MEDIA_ROOT, "face_encoding_data")
        files = os.listdir(face_encoding_dir_path)

        names = []

        for file in files:
            data = pickle.loads(open(os.path.join(face_encoding_dir_path, file), "rb").read())
            #Find path to the image you want to detect face and pass it here
            image = cv2.imread(captured_image_full_path)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            #convert image to Greyscale for haarcascade
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray,
                                                scaleFactor=1.1,
                                                minNeighbors=5,
                                                minSize=(60, 60),
                                                flags=cv2.CASCADE_SCALE_IMAGE)

            # the facial embeddings for face in input
            encodings = face_recognition.face_encodings(rgb)

            # loop over the facial embeddings incase
            # we have multiple embeddings for multiple faces
            for encoding in encodings:
                #Compare encodings with encodings in data["encodings"]
                #Matches contain array with boolean values and True for the embeddings it matches closely
                #and False for rest
                matches = face_recognition.compare_faces(data["encodings"], encoding)
                #set name =inknown if no encoding matches
                name = "Unknown"
                # check to see if we have found a match
                if True in matches:
                    #Find positions at which we get True and store them
                    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}
                    # loop over the matched indexes and maintain a count for
                    # each recognized face face
                    for i in matchedIdxs:
                        #Check the names at respective indexes we stored in matchedIdxs
                        name = data["names"][i]
                        #increase count for the name we got
                        counts[name] = counts.get(name, 0) + 1
                        #set name which has highest count
                        name = max(counts, key=counts.get)

                    # update the list of names
                    names.append(name)
                    print("roll no---------------->", names)
                    # loop over the recognized faces
                if len(names) != 0: break

        for index, roll_no in enumerate(names):
            try:
                with transaction.atomic():
                    student_obj = UserDetail.objects.filter(roll_no__iexact = roll_no).first()
                    attendance = Attendance.objects.create(user = student_obj,)
            except Exception as e:
                raise e

        return Response({
            # "success":[
                # names,
            # ]
            "roll_no": names
            }, status=status.HTTP_202_ACCEPTED)



# ! https://www.mygreatlearning.com/blog/face-recognition/
# ! take live image of user from camera from attendance.html template and throw it here and try to match it with the all users saved encoded data files and show roll no.
# ! for loop the encoding files
