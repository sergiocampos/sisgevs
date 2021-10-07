from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

# Register your models here.

class UserAdmin(BaseUserAdmin):

	fieldsets = (
		(None, {'fields': ('login', 'password', 'funcao', 'username', 'municipio', 'perfil', 'email','last_login', 'assinatura')}),
		('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 
			'groups', 'user_permissions')}),)
	add_fieldsets = (
		(
			None,
			{
				'classes': ('wide',),
				'fields': ('login', 'password1', 'password2')
			}
		),
	)
	list_display = ('login', 'funcao', 'username', 'municipio', 'perfil', 'email', 'is_staff', 'last_login')
	list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
	search_fields = ('login',)
	filter_horizontal = ('groups', 'user_permissions',)
	#add_form = CustomUserCreationForm
	#form = CustomUserChangeForm
	#model = User
	#list_display = ['id', 'username', 'email', 'cpf', 'funcao']

admin.site.register(User, UserAdmin)