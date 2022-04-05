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