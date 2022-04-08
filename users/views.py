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
        validator = UserDetail.objects.filter(email = email_var, password = password_var).last()
        # validator = auth.authenticate(email__iexact = email_var, password__iexact = password_var)
        if validator is None:
            return redirect('/users/login/error/')
        else:
            # https://learndjango.com/tutorials/django-login-and-logout-tutorial
            return redirect('/users/register/')

    else:
        return render(request, 'admin_login.html')


def ErrorLoginView(request):
    return render(request, 'error_login.html')


def UserRegisterView(request):
    return render(request, 'register_student.html')



# ? Logout: https://www.youtube.com/watch?v=geGwkBPcacg, https://www.youtube.com/watch?v=CTrVDi3tt8o