from core.models import CasoEsporotricose
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User

# Register your models here.

class UserAdmin(BaseUserAdmin):

	fieldsets = (
		(None, {'fields': ('login', 'password', 'funcao', 'username', 'municipio', 'perfil', 'email', 'telefone','last_login', 'assinatura', 'cpf')}),
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
# TODO descomentar para criar o grupo
#ct = ContentType.objects.get_for_model(CasoEsporotricose)
#acesso_esporo, acesso_esporo_criado = Group.objects.get_or_create(name='Acesso esporotricose')
#permission_esporotricose = Permission.objects.get(codename='acessa_esporotricose')
#acesso_esporo.permissions.add(permission_esporotricose)
