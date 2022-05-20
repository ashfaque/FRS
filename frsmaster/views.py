from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
from pdb import set_trace as bp
import os
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.conf import settings


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
        roll_no = request.POST['roll_no']
        image1 = request.FILES.get('image1', None)
        image2 = request.FILES.get('image2', None)
        image3 = request.FILES.get('image3', None)
        image4 = request.FILES.get('image4', None)
        image5 = request.FILES.get('image5', None)


        img1_extension = os.path.splitext(image1.name)[-1]
        img2_extension = os.path.splitext(image2.name)[-1]
        img3_extension = os.path.splitext(image3.name)[-1]
        img4_extension = os.path.splitext(image4.name)[-1]
        img5_extension = os.path.splitext(image5.name)[-1]


        for index in range(5):
            if os.path.exists(settings.FRS_MEDIA_ROOT + str(roll_no) + f"_{index+1}" + img1_extension):
                print(settings.FRS_MEDIA_ROOT + str(roll_no) + f"_{index+1}" + img1_extension)
                os.remove(settings.FRS_MEDIA_ROOT + str(roll_no) + f"_{index+1}" + img1_extension)


        img1_path = default_storage.save(settings.FRS_MEDIA_ROOT + str(roll_no) + "_1" + img1_extension, image1)
        img2_path = default_storage.save(settings.FRS_MEDIA_ROOT + str(roll_no) + "_2" + img2_extension, image2)
        img3_path = default_storage.save(settings.FRS_MEDIA_ROOT + str(roll_no) + "_3" + img3_extension, image3)
        img4_path = default_storage.save(settings.FRS_MEDIA_ROOT + str(roll_no) + "_4" + img4_extension, image4)
        img5_path = default_storage.save(settings.FRS_MEDIA_ROOT + str(roll_no) + "_5" + img5_extension, image5)

        detected_faces1 = detect_faces(img1_path)
        detected_faces2 = detect_faces(img2_path)
        detected_faces3 = detect_faces(img3_path)
        detected_faces4 = detect_faces(img4_path)
        detected_faces5 = detect_faces(img5_path)

        return Response({
            "success":[
                detected_faces1,
                detected_faces2,
                detected_faces3,
                detected_faces4,
                detected_faces5,
            ]
            }, status=status.HTTP_202_ACCEPTED)



# ! https://www.mygreatlearning.com/blog/face-recognition/
# ! take live image of user from camera from attendance.html template and throw it here and try to match it with the all users saved encoded data files and show roll no.













        # # print(f"email---------->{email_var}\npassword------------>{password_var}")
        # validator = UserDetail.objects.filter(email = email_var, password = password_var).last()
        # # validator = auth.authenticate(email__iexact = email_var, password__iexact = password_var)
        # if validator is None:
        #     return redirect('/users/login/error/')
        # else:
        #     # https://learndjango.com/tutorials/django-login-and-logout-tutorial
        #     return redirect('/users/register/')

    # else:
    #     return render(request, 'register_student.html')