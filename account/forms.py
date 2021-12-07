from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from .models import User
class CustomUserCreationForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('username', 'login', 'municipio', 'cpf', 'telefone')
	
	def usuario(self):
		user = self.cleaned_data('username')
		print('user')
		if User.objects.filter(username=user).exists():
			raise ValidationError('usuário já existe')

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('username', 'login')
