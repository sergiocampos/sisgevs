from django.db import models
from django.contrib.postgres.fields import ArrayField

from core.models import *

# Create your models here.

class Acidente(models.Model):

	#Informações Gerais do acidente
	data_acidente = models.DateField(blank=True, null=True)
	periodo_do_dia = models.CharField(max_length = 100, null=True, blank=True)
	dia_da_semana_ocorreu = models.CharField(max_length = 200, null=True, blank=True)
	ocorreu_dia_feriado = models.CharField(max_length = 100, null=True, blank=True)
	municipio_ocorrencia_acidente = models.CharField(max_length = 200, null=True, blank=True)
	bairro_ocorrencia_acidente = models.CharField(max_length = 200, null=True, blank=True)
	endereco_local_acidente = models.TextField(blank=True, default='', null=True)
	tipo_acidente = models.CharField(max_length = 100, null=True, blank=True)
	tipo_acidente_outros = models.CharField(max_length = 100, null=True, blank=True)
	tipos_veiculos_envolvidos = models.CharField(max_length = 100, null=True, blank=True)
	tipos_veiculos_envolvidos_outros = models.CharField(max_length = 100, null=True, blank=True)
	paciente_envolvido_acidente = models.CharField(max_length = 100, null=True, blank=True)
	presenca_sinais_embriagues = models.CharField(max_length = 100, null=True, blank=True)

	#Severidade do acidente e quantidade de vitimas
	houve_vitimas_fatais = models.CharField(max_length = 100, null=True, blank=True)
	numero_vitimas_fatais = models.IntegerField(blank=True, null=True)
	numero_feridos_envolvidos = models.IntegerField(blank=True, null=True)
	quadro_lesoes = models.CharField(max_length = 200, null=True, blank=True)
	em_caso_obito = models.CharField(max_length = 200, null=True, blank=True)

	#Equipe acionada para o local do acidente
	responsavel_prestar_apoio_local = ArrayField(models.CharField(max_length = 200, null=True, blank=True))
	responsavel_comentario = models.CharField(max_length = 200, null=True, blank=True)

	#Informações do paciente
	nome_paciente = models.CharField(max_length = 200, null=True, blank=True)
	data_nasc_paciente = models.DateField(blank=True, null=True)
	idade_paciente = models.IntegerField(blank=True, null=True)
	sexo_paciente = models.CharField(max_length = 50, null=True, blank=True)
	filiacao = models.CharField(max_length = 200, null=True, blank=True)
	endereco_paciente = models.CharField(max_length = 200, null=True, blank=True)
	contato_telefonico = models.CharField(max_length = 200, null=True, blank=True)
	cpf_paciente = models.CharField(max_length = 50, null=True, blank=True)
	cns_paciente = models.CharField(max_length = 50, null=True, blank=True)

	#Outras informações sobre o acidente
	paciente_referenciado_regulado_para_hospital = models.CharField(max_length = 20, null=True, blank=True)
	hospital = models.CharField(max_length = 200, null=True, blank=True)
	informacoes_complementares = models.TextField(blank=True, default='', null=True)

	#Unidade notificadora
	nome_hospital_ou_instituicao = models.CharField(max_length = 200, null=True, blank=True)
	nome_secretario_municipal_saude = models.CharField(max_length = 200, null=True, blank=True)
	cargo_funcao_notificador = models.CharField(max_length = 200, null=True, blank=True)
	contato_notificador = models.CharField(max_length = 200, null=True, blank=True)

	#Outros
	responsavel_pelas_informacoes = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
	responsavel_edicao = models.IntegerField(blank=True, null=True)
	gerencia = models.ForeignKey(Gerencia, on_delete=models.CASCADE, null=True)
	status_caso = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.responsavel_prestar_apoio_local


	class Meta:
		verbose_name_plural='Acidentes de Trânsito'