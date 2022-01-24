import re
from django.db import models
from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from core.models import Municipio


class UserManager(BaseUserManager):

	def _create_user(self, email, login, password, is_staff, is_superuser, **extra_fields):
		now = timezone.now()
		if not login:
			raise ValueError(('Um no com iniciais do hospital deve ser fornecido'))

		email = self.normalize_email(email)
		user = self.model(login=login, is_staff=is_staff, is_active=True, is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email=None, login=None, password=None, **extra_fields):
		return self._create_user(email, login, password, False, False, **extra_fields)

	def create_superuser(self, email, login, password, **extra_fields):
		user=self._create_user(email, login, password, True, True, **extra_fields)
		user.is_active=True
		user.save(using=self._db)
		return user

class User(AbstractBaseUser, PermissionsMixin):
	OPTIONS = [
		('admin', 'Admin'),
		('gerencia_executiva','Gerência Executiva'),
		('gerencia_regional', 'Gerência Regional de Saúde'),
		('gerencia_operacional', 'Gerência Operacional'),
		('area_tecnica', 'Área Técnica'),
		('chefia_nucleo', 'Chefia de Núcleo'),
		('municipal', 'Municipal'),
		('autocadastro', 'Autocadastro')
	]

	login = models.CharField(max_length = 200, help_text='Informe um login', unique=True)
	funcao = models.CharField(max_length=50, choices=OPTIONS, default='padrao')
	username = models.CharField(max_length=100, null=True, blank=True)
	cpf = models.CharField(max_length=11, null=True, blank=True)
	telefone = models.CharField(max_length=15, null=True, blank=True)
	#hospital = models.ForeignKey(Hospital, on_delete = models.CASCADE, default='', null=True)
	
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, null=True)
	unidade_saude = models.CharField(max_length=255, null=True, blank=True)
	perfil = models.CharField(max_length=255, null=True, blank=True)
	
	email = models.EmailField(_('email address'), max_length=255, null=True)
	assinatura = models.ImageField(blank=True, null=True, upload_to='media')
	first_name = models.CharField(_('first name'), max_length=30)
	last_name = models.CharField(_('last name'), max_length=30)
	is_superuser = models.BooleanField(default=False)
	is_staff = models.BooleanField(_('staff status'), default=False, 
		help_text=_('Define se o usuario pode fazer login neste site de administração.')) 
	is_active = models.BooleanField(_('active'), default=True, 
		help_text=_('Designa se esse usuário deve ser tratado como ativo. Desmarque isso ao invés de excluir conta.'))

	last_login = models.DateTimeField(null=True, blank=True)
	date_joined = models.DateTimeField(_('data adesão'), default=timezone.now)
	
	
	USERNAME_FIELD = 'login'
	CPF_FIELD = 'login'
	REQUIRED_FIELDS = ['email']

	objects = UserManager()

	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')

	def get_absolute_url(self):
		return "/users/%i/" % (self.pk)

	def get_login_hospital(self):
		return self.login

	def get_hospital(self):
		return self.hospital

	def get_full_name(self):
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		return self.first_name

	def email_user(self, subject, message, from_email=None):
		send_mail(subject, message, from_email, [self.email])

	def get_funcao_user(self):
		return self.funcao

	def __str__(self):
		return str(self.username)