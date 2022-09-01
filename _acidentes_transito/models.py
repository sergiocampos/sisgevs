from django.contrib.postgres.fields import ArrayField
      
from django.db import models
      
from core.models import *
      
class AcidentesTransito(models.Model):
    
  data_acidente = models.DateField(null=True, blank=True, unique=False)
  periodo_dia = models.CharField(max_length=255, null=True, blank=True, unique=False)
  que_dia_semana_ocorreu_acidente = models.CharField(max_length=255, null=True, blank=True, unique=False)
  acidente_ocorreu_dia_feriado = models.CharField(max_length=255, null=True, blank=True, unique=False)
  municipio_ocorrencia_acidente = models.CharField(max_length=255, null=True, blank=True, unique=False)
  endereco_local_acidente = models.CharField(max_length=255, null=True, blank=True, unique=False)
  tipo_acidente = models.CharField(max_length=255, null=True, blank=True, unique=False)
  tipos_veiculos_envolvidos_acidente = ArrayField(models.CharField(max_length=255, null=True, blank=True, unique=False))
  paciente_envolvido_acidente_era = models.CharField(max_length=255, null=True, blank=True, unique=False)
  vitima_apresenta_sinais_embriaguez_consumo_bebidas_alcoolicas = models.CharField(max_length=255, null=True, blank=True, unique=False)
  houve_vitimas_fatais = models.CharField(max_length=255, null=True, blank=True, unique=False)
  numeros_vitimas_fatais_envolvidas_acidente = models.CharField(max_length=255, null=True, blank=True, unique=False)
  numero_feridos_envolvidos_acidente = models.CharField(max_length=255, null=True, blank=True, unique=False)
  quadro_lesoes = models.CharField(max_length=255, null=True, blank=True, unique=False)
  caso_obito = models.CharField(max_length=255, null=True, blank=True, unique=False)
  quem_foi_responsavel_por_prestar_apoio_local = ArrayField(models.CharField(max_length=255, null=True, blank=True, unique=False))
  nome_paciente_sem_abreviacoes = models.CharField(max_length=255, null=True, blank=True, unique=False)
  data_nascimento = models.DateField(null=True, blank=True, unique=False)
  idade_paciente = models.IntegerField(null=True, blank=True, unique=False)
  sexo = models.CharField(max_length=255, null=True, blank=True, unique=False)
  nome_mae = models.CharField(max_length=255, null=True, blank=True, unique=False)
  endereco_paciente = models.CharField(max_length=255, null=True, blank=True, unique=False)
  contato_telefonico = models.CharField(max_length=50, null=True, blank=True, unique=False)
  cpf_paciente = models.CharField(max_length=50, null=True, blank=True, unique=False)
  cns_paciente = models.CharField(max_length=50, null=True, blank=True, unique=False)
  paciente_foi_referenciado_para_outro_hospital = models.CharField(max_length=255, null=True, blank=True, unique=False)
  qual_hospital = models.CharField(max_length=255, null=True, blank=True, unique=False)
  informacoes_complementares = models.CharField(max_length=255, null=True, blank=True, unique=False)
  nome_instituicao_hospital = models.CharField(max_length=255, null=True, blank=True, unique=False)
  nome_instituicao = models.CharField(max_length=255, null=True, blank=True, unique=False)
  nome_responsavel_pela_digitacao = models.CharField(max_length=255, null=True, blank=True, unique=False)
  cargo_funcao_notificador = models.CharField(max_length=255, null=True, blank=True, unique=False)
  contato_notificador = models.CharField(max_length=50, null=True, blank=True, unique=False)
  # Outros
  responsavel_pelas_informacoes = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
  responsavel_edicao = models.IntegerField(blank=True, null=True)
  gerencia = models.ForeignKey(Gerencia, on_delete=models.CASCADE, null=True)
  status_caso = models.CharField(max_length=50, null=True, blank=True)