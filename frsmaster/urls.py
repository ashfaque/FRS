from django.urls import path, include
from . import views

urlpatterns = [
    path('apply_frs/', views.FMApplyFRSView, name = 'applyfrs'),
]