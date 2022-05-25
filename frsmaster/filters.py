import django_filters
from .models import Attendance

class AttendanceFilter(django_filters.FilterSet):
    class Meta:
        model = Attendance
        fields = '__all__'
        exclude = ['is_deleted', 'deleted_at', 'deleted_by', 'date']    # * TO ADD DATE FILTER REMOVE DATE FROM HERE.