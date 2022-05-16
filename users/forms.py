from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import UserDetail

class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = UserDetail
		fields = '__all__'