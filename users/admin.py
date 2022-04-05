from django.contrib import admin
from users.models import *
# Register your models here.

@admin.register(UserDetail)
class UserDetail(admin.ModelAdmin):
    list_display = [field.name for field in UserDetail._meta.fields]
    search_fields = ('id', 'email', 'username', 'user_type', 'phone_no', 'college__name', 'department__name', 'sub_department__name', 'is_deleted')