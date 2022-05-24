from django.contrib import admin
from .models import *

# Register your models here.

# @admin.register(FRSUserMapping)
# class FRSUserMapping(admin.ModelAdmin):
    # list_display = [field.name for field in FRSUserMapping._meta.fields]
    # search_fields = ('user__first_name','user__last_name', 'frs_data', 'created_at', 'is_deleted', 'deleted_at', 'deleted_by__first_name', 'deleted_by__last_name')


@admin.register(Attendance)
class Attendance(admin.ModelAdmin):
    list_display = [field.name for field in Attendance._meta.fields]
    search_fields = ('user__first_name','user__last_name', 'date', 'is_deleted', 'deleted_at', 'deleted_by__first_name', 'deleted_by__last_name')