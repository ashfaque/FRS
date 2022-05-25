from django.urls import path, include
from . import views

urlpatterns = [
	path('login/', views.UserLoginView, name = 'login'),
	path('login/error/', views.ErrorLoginView, name = 'error_login'),
	path('logout/', views.UserLogoutView, name = 'logout'),
	# path('register/', views.UserRegisterView, name = 'register'),
	path('attendance/', views.UserAttendanceView, name = 'attendance'),
	# path('attendance/report/', views.UserAttendanceReportView, name = 'attendance_report'),
]