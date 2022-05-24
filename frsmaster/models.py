from django.db import models
from users.models import UserDetail
from django.utils import timezone
from django.conf import settings

# Create your models here.

# class FRSUserMapping(models.Model):
#     user = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name='fum_user')
#     frs_data = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     is_deleted = models.BooleanField(default=False)
#     deleted_at = models.DateTimeField(blank=True, null=True)
#     deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name='fum_deleted_by')

#     def __str__(self):    # ? Shows the details of specific fields if a user prints the 'instance' of this model.
#         return str(self.id)

#     class Meta:
#         db_table = 'frs_user_mapping'


class Attendance(models.Model):
    user = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name='attendance_user')
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_deleted= models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name='attendance_deleted_by')

    def __str__(self):    # ? Shows the details of specific fields if a user prints the 'instance' of this model.
        return str(self.id)

    class Meta:
        db_table = 'attendance'