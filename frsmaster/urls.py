from django.urls import path, include
from . import views

urlpatterns = [
    path('apply_frs/', views.FMApplyFRSView, name = 'applyfrs'),
    path('attendance/report/', views.FMAttendanceReportView, name = 'attendance_report'),
]