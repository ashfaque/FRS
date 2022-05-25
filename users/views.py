from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import redirect
from users.models import UserDetail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def UserLoginView(request):
    if request.user.is_authenticated:    # ? If already logged in then it will redirect to landing page.
        return redirect('/frsmaster/attendance/report/')
    if request.method == 'POST':
        username_var = request.POST['username']
        password_var = request.POST['password']
        # print(f"email---------->{email_var}\npassword------------>{password_var}")
        # validator = UserDetail.objects.filter(email = email_var, password = password_var).last()
        # validator = auth.authenticate(email__iexact = email_var, password__iexact = password_var)
        user = UserDetail.objects.filter(username__iexact=username_var).values_list('username', flat=True).last()
        if user:
            user_obj = UserDetail.objects.get(username__iexact=username_var)
            # if validator is not None:
            if user_obj and user_obj.check_password(password_var):
                user_authenticate = authenticate(request, username = username_var, password = password_var)
                if user_authenticate is not None:
                    login(request, user_authenticate)
                    # return redirect('/users/register/')
                    return redirect('/frsmaster/attendance/report/')
                else:
                    messages.info(request, 'Username or Password is incorrect')
            else:
                return redirect('/users/login/error/')
        else:
            return redirect('/users/login/error/')
            # https://learndjango.com/tutorials/django-login-and-logout-tutorial

    context = {}
    return render(request, 'admin_login.html', context)
    # return render(request, 'admin_login.html')

def ErrorLoginView(request):
    return render(request, 'error_login.html')


# def UserRegisterView(request):
#     return render(request, 'register_student.html')


def UserAttendanceView(request):
    return render(request, 'attendance.html')


# @login_required(login_url = 'login')
# def UserAttendanceReportView(request):
#     return render(request, 'attendance_report.html')


@login_required(login_url = 'login')
def UserLogoutView(request):
    logout(request)
    return redirect('login')


# ? Logout: https://www.youtube.com/watch?v=geGwkBPcacg, https://www.youtube.com/watch?v=CTrVDi3tt8o