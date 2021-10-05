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

	#Notificação Individual
	nome_paciente
	data_nascimento_paciente
	idade_paciente
	sexo_paciente
	paciente_gestante
	raca_paciente
	escolaridade_paciente
	cantao_sus_paciente
	nome_mae_paciente

	#dados de residencia
	cep_residencia
	uf_residencia
	municipio_residencia
	bairro_residencia
	codigo_ibge_residencia
	rua_residencia
	numero_residencia
	complemento_residencia
	distrito_residencia
	ponto_referencia_residencia
	telefone_residencia
	zona_residencia
	pais_residencia

	#antecedentes Epidemiologicos
	data_investigacao
	ocupacao
	ambientes_frequentados
	animais_que_teve_contato
	natureza_contato_animais
	relacao_animal_doente
	exerce_atividade_contato_plantas
	historico_contato_material

	#Dados clínicos
	presenca_lesao_pele
	natureza_lesao
	local_lesao
	diagnostico_forma_extrac_doenca
	localizacao_forma_extrac_doenca

	#Dados Laboratoriais
	houve_coleta_material
	data_coleta
	resultado_isolamento
	agente
	histopatologia

	data_exame1
	descricao_exame_1
	resultado_exame1
	
	data_exame2
	descricao_exame_2
	resultado_exame2
	
	data_exame3
	descricao_exame_3
	resultado_exame3

	#Tratamento
	data_inicio_tratamento1
	droga_administrada1
	esquema_terapeutico1

	data_inicio_tratamento2
	droga_administrada2
	esquema_terapeutico2

	data_inicio_tratamento3
	droga_administrada3
	esquema_terapeutico3

	hospitalizacao
	data_internacao
	data_da_alta
	uf_hospitalizacao
	municipio_hospitalizacao
	codigo_ibge_hospitalizacao
	nome_hospital_hospitalizacao
	codigo_hospital_hospitalizacao?????

	#Conclusao
	classificacao_final
	criterio_confirmacao
	caso_autoctone_municipio_residencia
	uf_caso_autoctone
	pais_caso_autoctone
	municipio_caso_autoctone
	codigo_ibge_caso_autoctone
	distrito_caso_autoctone
	bairro_caso_autoctone
	area_provavel_infeccao_caso_autoctone
	ambiente_infeccao_caso_autoctone
	doenca_rel_trabalho_caso_autoctone
	evolucao_caso
	data_encerramento

	#Observacao
	observacao

	#Investigador
	nome_investigador
	funcao_investigador
	email_investigador
	telefone_investigador
	conselho_classe_investigador