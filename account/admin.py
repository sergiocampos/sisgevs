from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.models import CasoEsporotricose
from .forms import CustomUserCreationForm, CustomUserChangeForm
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
""" ct = ContentType.objects.get_for_model(CasoEsporotricose)
group_area_tecnica, area_tecnica_criada = Group.objects.get_or_create(name='Área tecnica esporotricose')
group_chefia_nucleo, chefia_nucleo_criada = Group.objects.get_or_create(name='Chefia núcleo esporotricose')
group_ger_operacional, ger_operacional_criada = Group.objects.get_or_create(name='Gerencia operacional esporotricose')
permission_esporotricose = Permission.objects.get(codename='acessa_esporotricose')
group_area_tecnica.permissions.add(permission_esporotricose)
group_chefia_nucleo.permissions.add(permission_esporotricose)
group_ger_operacional.permissions.add(permission_esporotricose) """
