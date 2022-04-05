from django.db import models

# Create your models here.

class College(models.Model):
    code = models.CharField(max_length=100, default='FIEM', unique=True)  # not editable
    name = models.CharField(max_length=100, default='Future Institute of Engineering and Management')
    address = models.TextField(blank=True, null=True)
    short_name = models.CharField(max_length=100, blank=True, null=True)
    email_id_1 = models.CharField(max_length=100, blank=True, null=True)
    email_id_2 = models.CharField(max_length=100, blank=True, null=True)

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

    def __str__(self):
        # return str(self.id)
        return str(self.code)

    class Meta:
        db_table = 'master_department'
