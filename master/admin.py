from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(College)
class College(admin.ModelAdmin):
    list_display = [field.name for field in College._meta.fields]
    search_fields = ('name', 'code')


@admin.register(Department)
class Department(admin.ModelAdmin):
    list_display = [field.name for field in Department._meta.fields]
    search_fields = ('name', 'code', 'college__name',)