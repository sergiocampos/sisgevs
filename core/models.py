from operator import truediv
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

from localflavor.br.br_states import STATE_CHOICES

# Create your models here.

class UserProfileInfo(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	#portfolio_site = models.URLField(blank=True)
	#profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

	def __str__(self):
		return self.user.username



class Macrorregiao(models.Model):
	nome = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.nome


class Gerencia(models.Model):
	nome = models.CharField(max_length=200, null=True)
	macrorregiao = models.ForeignKey(Macrorregiao, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.nome

################ models para select ######################################

class Municipio(models.Model):
	nome = models.CharField(max_length=200, null=True)
	gerencia = models.ForeignKey(Gerencia, on_delete=models.CASCADE, null=True)
	#uf = models.CharField(max_length=200, choices=STATE_CHOICES)
	ibge = models.CharField(max_length=10, null=True)

	def __str__(self):
		return self.nome

	class Meta:
		ordering = ('nome',)
		verbose_name = 'cidade'
		verbose_name_plural = 'cidades'



class CodigoIbge(models.Model):
	codigo = models.CharField(max_length=200, null=True)
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)

	def __str__(self):
		return self.codigo

	class Meta:
		ordering = ('codigo',)
		verbose_name = 'ibge'
		verbose_name_plural = 'ibges'


##########################################################################


class Regiao(models.Model):
	nome = models.CharField(max_length=200, null=True)
	descricao = models.CharField(max_length=200, null=True)
	gerencia = models.ForeignKey(Gerencia, on_delete=models.CASCADE, null=True)
	macrorregiao = models.ForeignKey(Macrorregiao, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.nome


class UnidadeSaude(models.Model):
	nome = models.CharField(max_length=200, null=True)
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, null=True)
	cnes = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name_plural = 'Unidades de Saúde'


class Estado(models.Model):
	uf = models.IntegerField(blank=True, null=True)
	nome = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.nome


class MunicipioBr(models.Model):
	nome = models.CharField(max_length=200, null=True)
	uf = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True)
	ibge = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.nome

#############Tabela usada para selects de caso autoctone################################

class Municipios(models.Model):
	nome = models.CharField(max_length=200, null=True)
	uf = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True)
	ibge = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.nome


class Distrito(models.Model):
	nome = models.CharField(max_length=200, null=True)
	municipio = models.ForeignKey(MunicipioBr, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.nome


class JoinMunicipioIbgeUnidadeSaude(models.Model):
	unidade_saude = models.ForeignKey(UnidadeSaude, on_delete=models.CASCADE, null=True)
	ibge = models.ForeignKey(CodigoIbge, on_delete=models.CASCADE, null=True)
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, null=True)


class JoinDistritoMunicipioIbgeEstado(models.Model):
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True)
	ibge = models.ForeignKey(CodigoIbge, on_delete=models.CASCADE, null=True)
	municipio = models.ForeignKey(MunicipioBr, on_delete=models.CASCADE, null=True)
	distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE, null=True)
