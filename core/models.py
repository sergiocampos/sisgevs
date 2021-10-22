from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

from localflavor.br.br_states import STATE_CHOICES

# Create your models here.

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
	uf = models.CharField(max_length=200, choices=STATE_CHOICES)

	def __str__(self):
		return self.nome


class CodigoIbge(models.Model):
	codigo = models.CharField(max_length=200, null=True)
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)

	def __str__(self):
		return self.codigo


##########################################################################


class Regiao(models.Model):
	nome = models.CharField(max_length=200, null=True)
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



################# models de doenças ######################################

class CasoEsporotricose(models.Model):

	responsavel_pelas_informacoes = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

	tipo_notificacao = models.CharField(max_length = 200, null=True, blank=True)
	agravo_doenca = models.CharField(max_length = 200, null=True, blank=True)
	codigo_cib10 = models.CharField(max_length = 200, null=True, blank=True)
	data_notificacao = models.DateField(blank=True, null=True)
	estado = models.CharField(max_length = 100, null=True, blank=True)
	
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
	codigo_ibge = models.ForeignKey(CodigoIbge, on_delete=models.CASCADE)

	data_primeiros_sintomas = models.DateField(blank=True, null=True)
	unidade_saude = models.CharField(max_length = 200, null=True, blank=True)

	#Notificação Individual
	nome_paciente = models.CharField(max_length = 200, null=True, blank=True)
	data_nascimento_paciente = models.DateField(blank=True, null=True)
	idade_paciente = models.IntegerField(blank=True, null=True)
	sexo_paciente = models.CharField(max_length = 20, null=True, blank=True)
	paciente_gestante = models.CharField(max_length = 200, null=True, blank=True)
	raca_paciente = models.CharField(max_length = 20, null=True, blank=True)
	escolaridade_paciente = models.CharField(max_length = 100, null=True, blank=True)
	cantao_sus_paciente = models.CharField(max_length = 100, null=True, blank=True)
	nome_mae_paciente = models.CharField(max_length = 200, null=True, blank=True)

	#dados de residencia
	cep_residencia = models.CharField(max_length = 100, null=True, blank=True)
	uf_residencia = models.CharField(max_length = 100, null=True, blank=True)
	municipio_residencia = models.CharField(max_length = 200, null=True, blank=True)
	bairro_residencia = models.CharField(max_length = 200, null=True, blank=True)
	codigo_ibge_residencia = models.CharField(max_length = 50, null=True, blank=True)
	rua_residencia = models.CharField(max_length = 200, null=True, blank=True)
	numero_residencia = models.CharField(max_length = 100, null=True, blank=True)
	complemento_residencia = models.CharField(max_length = 200, null=True, blank=True)
	distrito_residencia = models.CharField(max_length = 200, null=True, blank=True)
	ponto_referencia_residencia = models.CharField(max_length = 200, null=True, blank=True)
	telefone_residencia = models.CharField(max_length = 100, null=True, blank=True)
	zona_residencia = models.CharField(max_length = 100, null=True, blank=True)
	pais_residencia = models.CharField(max_length = 100, null=True, blank=True)

	#antecedentes Epidemiologicos
	data_investigacao = models.DateField(blank=True, null=True)
	ocupacao = models.CharField(max_length = 100, null=True, blank=True)
	ambientes_frequentados = ArrayField(models.CharField(max_length=100), blank=True, null=True)
	animais_que_teve_contato = ArrayField(models.CharField(max_length=100), blank=True, null=True)
	natureza_contato_animais = ArrayField(models.CharField(max_length=200), blank=True, null=True)
	relacao_animal_doente = ArrayField(models.CharField(max_length=200), blank=True, null=True)
	exerce_atividade_contato_plantas = models.CharField(max_length = 100, null=True, blank=True)
	historico_contato_material = models.CharField(max_length = 100, null=True, blank=True)

	#Dados clínicos
	presenca_lesao_pele = models.CharField(max_length = 100, null=True, blank=True)
	natureza_lesao = ArrayField(models.CharField(max_length=200), blank=True, null=True)
	local_lesao = ArrayField(models.CharField(max_length=200), blank=True, null=True)
	diagnostico_forma_extrac_doenca = models.CharField(max_length = 100, null=True, blank=True)
	localizacao_forma_extrac_doenca = models.CharField(max_length = 200, null=True, blank=True)

	#Dados Laboratoriais
	houve_coleta_material = models.CharField(max_length = 10, null=True, blank=True)
	data_coleta = models.DateField(blank=True, null=True)
	resultado_isolamento = models.CharField(max_length = 200, null=True, blank=True)
	agente = models.CharField(max_length = 200, null=True, blank=True)
	histopatologia = models.CharField(max_length = 100, null=True, blank=True)

	data_exame1 = models.DateField(blank=True, null=True)
	descricao_exame_1 = models.CharField(max_length = 200, null=True, blank=True)
	resultado_exame1 = models.CharField(max_length = 200, null=True, blank=True)
	
	data_exame2 = models.DateField(blank=True, null=True)
	descricao_exame_2 = models.CharField(max_length = 200, null=True, blank=True)
	resultado_exame2 = models.CharField(max_length = 200, null=True, blank=True)
	
	data_exame3 = models.DateField(blank=True, null=True)
	descricao_exame_3 = models.CharField(max_length = 200, null=True, blank=True)
	resultado_exame3 = models.CharField(max_length = 200, null=True, blank=True)

	#Tratamento
	data_inicio_tratamento1 = models.DateField(blank=True, null=True)
	droga_administrada1 = models.CharField(max_length = 200, null=True, blank=True)
	esquema_terapeutico1 = models.CharField(max_length = 100, null=True, blank=True)

	data_inicio_tratamento2 = models.DateField(blank=True, null=True)
	droga_administrada2 = models.CharField(max_length = 200, null=True, blank=True)
	esquema_terapeutico2 = models.CharField(max_length = 100, null=True, blank=True)

	data_inicio_tratamento3 = models.DateField(blank=True, null=True)
	droga_administrada3 = models.CharField(max_length = 200, null=True, blank=True)
	esquema_terapeutico3 = models.CharField(max_length = 100, null=True, blank=True)

	hospitalizacao = models.CharField(max_length = 10, null=True, blank=True)
	data_internacao = models.DateField(blank=True, null=True)
	data_da_alta = models.DateField(blank=True, null=True)
	uf_hospitalizacao = models.CharField(max_length = 10, null=True, blank=True)
	municipio_hospitalizacao = models.CharField(max_length = 200, null=True, blank=True)
	codigo_ibge_hospitalizacao = models.CharField(max_length = 100, null=True, blank=True)
	nome_hospital_hospitalizacao = models.CharField(max_length = 200, null=True, blank=True)

	#Conclusao
	classificacao_final = models.CharField(max_length = 200, null=True, blank=True)
	criterio_confirmacao = models.CharField(max_length = 200, null=True, blank=True)
	caso_autoctone_municipio_residencia = models.CharField(max_length = 200, null=True, blank=True)
	uf_caso_autoctone = models.CharField(max_length = 10, null=True, blank=True)
	pais_caso_autoctone = models.CharField(max_length = 100, null=True, blank=True)
	municipio_caso_autoctone = models.CharField(max_length = 200, null=True, blank=True)
	codigo_ibge_caso_autoctone = models.CharField(max_length = 50, null=True, blank=True)
	distrito_caso_autoctone = models.CharField(max_length = 200, null=True, blank=True)
	bairro_caso_autoctone = models.CharField(max_length = 200, null=True, blank=True)
	area_provavel_infeccao_caso_autoctone = models.CharField(max_length = 100, null=True, blank=True)
	ambiente_infeccao_caso_autoctone = models.CharField(max_length = 100, null=True, blank=True)
	doenca_rel_trabalho_caso_autoctone = models.CharField(max_length = 100, null=True, blank=True)
	evolucao_caso = models.CharField(max_length = 100, null=True, blank=True)
	data_obito = models.DateField(blank=True, null=True)
	data_encerramento = models.DateField(blank=True, null=True)

	#Observacao
	observacao = models.TextField(blank=True, default='', null=True)

	#Investigador
	nome_investigador = models.CharField(max_length = 200, null=True, blank=True)
	funcao_investigador = models.CharField(max_length = 100, null=True, blank=True)
	email_investigador = models.CharField(max_length = 100, null=True, blank=True)
	telefone_investigador = models.CharField(max_length = 100, null=True, blank=True)
	conselho_classe_investigador = models.CharField(max_length = 100, null=True, blank=True)

	def __str__(self):
		return self.tipo_notificacao