import os

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
    path = '{0}/{1}/{2}/{3}'.format(app_name, model_name, dir, filename)
    return path


def save_face_data_while_creating_user(pk, instance, action='create', remarks=''):
    # ! Apply FRS here and save the string data somewhere in DB.
    from users.models import UserDetail
    # UserActionLog.objects.create(user=user, action=action, table_name=table_name, entity_id=entity_id, remarks=remarks)
    profile_image_dict = UserDetail.objects.filter(id = pk).values("profile_img").last()
    if profile_image_dict['profile_img']:
        print("###############  APPLY FRS HERE  ########################----->",profile_image_dict['profile_img'])
