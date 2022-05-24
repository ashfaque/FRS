from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class College(models.Model):
    code = models.CharField(max_length=100, default='FIEM', unique=True)  # not editable
    name = models.CharField(max_length=100, default='Future Institute of Engineering and Management')
    address = models.TextField(blank=True, null=True)
    short_name = models.CharField(max_length=100, blank=True, null=True)
    email_id_1 = models.CharField(max_length=100, blank=True, null=True)
    email_id_2 = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, blank=True, null=True, related_name='col_created_by')
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name='col_updated_by')
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name='col_deleted_by')
    

    def __str__(self):
        # return str(self.id)
        return str(self.code)

    class Meta:
        db_table = 'master_college'


class Department(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='d_college')
    code = models.CharField(max_length=100, default='CA', unique=True)
    name = models.CharField(max_length=100)
    parent = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, blank=True, null=True, related_name='dept_created_by')
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name='dept_updated_by')
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name='dept_deleted_by')

    def __str__(self):
        # return str(self.id)
        return str(self.code)

    class Meta:
        db_table = 'master_department'
