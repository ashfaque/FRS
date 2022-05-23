from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import redirect
from users.models import UserDetail

# Create your views here.


def UserLoginView(request):
    if request.method == 'POST':
        email_var = request.POST['email']
        password_var = request.POST['password']
        # print(f"email---------->{email_var}\npassword------------>{password_var}")
        # validator = UserDetail.objects.filter(email = email_var, password = password_var).last()
        # validator = auth.authenticate(email__iexact = email_var, password__iexact = password_var)
        user = UserDetail.objects.get(email__iexact=email_var)
        # if validator is not None:
        if user and user.check_password(password_var):
            # return redirect('/users/register/')
            return redirect('/users/attendance/')
        else:
            return redirect('/users/login/error/')
            # https://learndjango.com/tutorials/django-login-and-logout-tutorial


    else:
        return render(request, 'admin_login.html')


def ErrorLoginView(request):
    return render(request, 'error_login.html')


# def UserRegisterView(request):
#     return render(request, 'register_student.html')

def UserAttendanceView(request):
    return render(request, 'attendance.html')



# ? Logout: https://www.youtube.com/watch?v=geGwkBPcacg, https://www.youtube.com/watch?v=CTrVDi3tt8o