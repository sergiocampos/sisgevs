from django.db import models

# Create your models here.

class CodigoIbge(models.Model):
	codigo = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.codigo


class Municipio(models.Model):
	nome = models.CharField(max_length=200, null=True)
	ibge = models.ForeignKey(CodigoIbge, on_delete=models.CASCADE)

	def __str__(self):
		return self.nome


class Estado(models.Model):
	nome = models.CharField(max_length=200, null=True)
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
	codigo_ibge = models.ForeignKey(CodigoIbge, on_delete=models.CASCADE)

	def __str__(self):
		return self.nome


class UnidadeSaude(models.Model):
	nome = models.CharField(max_length=200, null=True)
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
	#codigo_ibge = models.ForeignKey(CodigoIbge, on_delete=models.CASCADE)
	#estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

	def __str__(self):
		return self.nome

################# models para macrorregião e gerencia ######################

class Regiao(models.Model):
	nome = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.nome



class Gerencia(models.Model):
	nome = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.nome


class Macrorregiao(models.Model):
	nome = models.CharField(max_length=200, null=True)
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
	codigo_ibge = models.ForeignKey(CodigoIbge, on_delete=models.CASCADE)

	def __str__(self):
		return self.nome


################# models de doenças ######################################

class CasoEsporotricose(models.Model):
	tipo_notificacao
	agravo_doenca
	codigo_cib10
	data_notificacao

	estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
	codigo_ibge = models.ForeignKey(CodigoIbge, on_delete=models.CASCADE)

	data_primeiros_sintomas
	unidade_saude