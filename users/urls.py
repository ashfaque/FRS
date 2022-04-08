from django.urls import path, include
from . import views

urlpatterns = [
	path('login/', views.UserLoginView, name = 'login'),
	path('login/error/', views.ErrorLoginView, name = 'error_login'),
	path('register/', views.UserRegisterView, name = 'register'),
]