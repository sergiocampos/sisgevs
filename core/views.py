from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash, login, authenticate, logout

from django.core.paginator import Paginator

from django.http import HttpResponse, HttpResponseRedirect
import os
from datetime import datetime

from .models import *

# Create your views here.

def login_page(request):
	return render(request, 'login_page.html')


@csrf_protect
def login_submit(request):
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			return render(request, 'login_page.html')
			#messages.error(request, 'Usuário e/ou senha inválido!')
	return redirect('/login/')


@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/login/')


@login_required
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			messages.success(request, _('Your password was successfully updated!'))
			return redirect('/')
		else:
			messages.error(request, _('Please correct the error below.'))
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'change_password.html', {'form': form})


@login_required(login_url='/login/')
def set_login_page(request):
	return redirect('index')



@login_required(login_url='/login/')
def index(request):
	return render(request, 'index.html')



@login_required(login_url='/login/')
def main(request):
	return render(request, 'main.html')



@login_required(login_url='/login/')
def all_forms(request):
	return render(request, 'all_forms.html')



@login_required(login_url='/login/')
def informar_dados_ficha(request):
	return render(request, 'informar_dados_ficha.html')


@login_required(login_url='/login/')
def localizar_paciente_nome(request):
	return render(request, 'localizar_paciente_nome.html')


@login_required(login_url='/login/')
def set_localizar_paciente_nome(request):
	return render(request, 'resultado_search_caso_nome.html')



###########View Renderiza a ficha para impressão######################################################
@login_required(login_url='/login/')
def download_ficha(request):
	file_path = os.path.join(settings.MEDIA_ROOT, 'ficha_investigacao_esporotricose(1).pdf')
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/pdf")
			response['Content-Disposition'] = 'inline; filename' + os.path.basename(file_path)
			return response


@login_required(login_url='/login/')
def caso_view(request, id):
	registro = CasoEsporotricose.objects.get(id=id)
	municipio_id = registro.municipio
	municipio = Municipio.objects.get(id=municipio_id)
	ibge = municipio.ibge
	return render(request, 'caso_view.html', {'registro':registro, 'municipio':municipio, 'ibge':ibge})


@login_required(login_url='/login/')
def caso_view_detail(request):
	return render(request, 'caso_view_detail.html')


@login_required(login_url='/login/')
def caso_esporotricose_create(request):
	estados = Estado.objects.all().order_by('nome')
	municipios = Municipio.objects.all().order_by('nome')
	unidades_saude = []
	codigos_ibge = []
	return render(request, 'caso_esporotricose_create.html', {'municipios':municipios, 'unidades_saude':unidades_saude, 
		'codigos_ibge':codigos_ibge, 'estados':estados})

#############################views ajax dados gerais#####################################

@login_required(login_url='/login/')
def ajax_load_unidadesaude(request):
	municipio_id = request.GET.get('municipio_id')
	#cod_ibge = JoinMunicipioIbgeUnidadeSaude.objects.filter(municipio=municipio).all()
	cod_ibge = UnidadeSaude.objects.filter(municipio_id=municipio_id).all()
	
	return render(request, 'unidades_saude_ajax.html', {'cod_ibge':cod_ibge})


@login_required(login_url='/login/')
def ajax_load_ibge(request):
	municipio_id = request.GET.get('municipio_id')
	codigo = CodigoIbge.objects.filter(municipio_id=municipio_id).values()

	return render(request, 'ibge_ajax.html', {'codigo':codigo})


#############################view do ajax para hospitalização#################################
@login_required(login_url='/login/')
def ajax_hospitalizacao(request):
	municipio_id = request.GET.get('municipio_id')
	cod_ibge = UnidadeSaude.objects.filter(municipio_id=municipio_id).all().order_by('nome')
	
	return render(request, 'hospitalizacao_ajax.html', {'cod_ibge':cod_ibge})


@login_required(login_url='/login/')
def ajax_hospitalizacao_ibge(request):
	municipio_id = request.GET.get('municipio_id')
	codigo = CodigoIbge.objects.filter(municipio_id=municipio_id).values()

	return render(request, 'hospitalizacaoibge_ajax.html', {'codigo':codigo})


########################## view para caso autoctone ##########################################
@login_required(login_url='/login/')
def ajax_autoctone_uf(request):
	uf_id = request.GET.get('municipio_id')
	#cod_ibge = JoinMunicipioIbgeUnidadeSaude.objects.filter(municipio=municipio).all()
	municipio = MunicipioBr.objects.filter(uf_id=uf_id).all()
	
	return render(request, 'municipios_estado_ajax.html', {'municipio':municipio})


@login_required(login_url='/login/')
def ajax_autoctone_municipio(request):
	id = request.GET.get('municipio_id')
	#cod_ibge = JoinMunicipioIbgeUnidadeSaude.objects.filter(municipio=municipio).all()
	municipio = Municipios.objects.get(id=id)
	ibge = municipio.ibge
	return render(request, 'municipios_ibge_ajax.html', {'ibge':ibge})


@login_required(login_url='/login/')
def ajax_autoctone_distrito(request):
	municipio_id = request.GET.get('municipio_id')
	#cod_ibge = JoinMunicipioIbgeUnidadeSaude.objects.filter(municipio=municipio).all()
	distrito = Distrito.objects.filter(municipio_id=municipio_id)
	return render(request, 'municipios_distrito_ajax.html', {'distrito':distrito})

##############################end#############################################################


@login_required(login_url='/login/')
def my_datas(request):
	municipio_id_user = request.user.municipio_id
	municipio_user = Municipio.objects.get(id=municipio_id_user)
	#municipio_nome = municipio_user.nome
	if request.user.perfil == 'admin':
		registros = CasoEsporotricose.objects.all()
		paginator = Paginator(registros, 6)
		page = request.GET.get('page')
		regs = paginator.get_page(page)
		return render(request, 'my_datas.html', {'regs':regs})

	if request.user.perfil == 'gerencia':
		gerencia_user = municipio_user.gerencia
		registros = CasoEsporotricose.objects.filter(gerencia=gerencia_user)
		
		return render(request, 'my_datas.html', {'registros':registros})

	if request.user.perfil == 'municipio':
		registros = CasoEsporotricose.objects.filter(municipio=municipio_id_user)
		return render(request, 'my_datas.html', {'registros':registros})
	

@login_required(login_url='/login/')
def ficha_caso_esporotricose_preencher(request):
	return render(request, 'ficha_caso_esporotricose_preencher.html')

@login_required(login_url='/login/')
def ficha_caso_esporotricose_preenchido(request):
	return render(request, 'ficha_caso_esporotricose_preenchido.html')


def remove_caso_esporotricose(request, id):
	caso_esporotricose = CasoEsporotricose.objects.get(id=id)
	caso_esporotricose.delete()
	return redirect('my_datas')

@login_required(login_url='/login/')
def set_caso_esporotricose_create(request):
	print("entrou no set caso esporotricose")
	responsavel_pelas_informacoes = request.user

	#Dados Gerais
	tipo_notificacao = request.POST.get('tipo_notificacao')
	agravo_doenca = request.POST.get('agravo_doenca')
	codigo_cib10 = request.POST.get('codigo_cid')
	
	data_notificacao_cap = request.POST.get('data_notificacao')
	
	if data_notificacao_cap == '' or data_notificacao_cap == None:
		data_notificacao = None
	else:
		data_notificacao = datetime.strptime(data_notificacao_cap, '%Y-%m-%d').date()

	
	estado = request.POST.get('uf_notificacao')
	
	municipio_cap = request.POST.get('municipio_notificacao')
	if municipio_cap == '' or municipio_cap == None:
		municipio = None
	else:
		municipio = int(municipio_cap)

	municipio_id = municipio
	municipio_ = Municipio.objects.get(id=municipio_id)


	gerencia = municipio_.gerencia

	codigo_ibge = request.POST.get('codigo_ibge_dados_gerais')
	
	data_primeiros_sintomas_cap = request.POST.get('data_primeiros_sintomas')
	if data_primeiros_sintomas_cap == '' or data_primeiros_sintomas_cap == None:
		data_primeiros_sintomas = None
	else:
		data_primeiros_sintomas = datetime.strptime(data_primeiros_sintomas_cap, '%Y-%m-%d').date()

	
	unidade_saude = request.POST.get('unidade_saude')
	unidade_saude_outro = request.POST.get('unidade_saude_outro')
	
	#notificação individual
	nome_paciente = request.POST.get('nome_paciente').upper()
	
	data_nascimento_paciente_cap = request.POST.get('data_nasc')
	if data_nascimento_paciente_cap == '' or data_nascimento_paciente_cap == None:
		data_nascimento_paciente = None
	else:
		data_nascimento_paciente = datetime.strptime(data_nascimento_paciente_cap, '%Y-%m-%d').date()

	sexo_paciente = request.POST.get('sexo')
	
	idade_paciente_cap = request.POST.get('result')
	if idade_paciente_cap == '' or idade_paciente_cap == None:
		idade_paciente = None
	else:
		idade_paciente = int(idade_paciente_cap)

	paciente_gestante = request.POST.get('gestacao')
	raca_paciente = request.POST.get('raca')
	escolaridade_paciente = request.POST.get('escolaridade')
	cartao_sus_paciente = request.POST.get('cartao_sus')
	nome_mae_paciente = request.POST.get('nome_mae').upper()
	
	#Dados Residencia
	cep_residencia = request.POST.get('cep_residencia')
	uf_residencia = request.POST.get('uf_residencia')
	municipio_residencia = request.POST.get('cidade_residencia')
	bairro_residencia = request.POST.get('bairro_residencia')
	codigo_ibge_residencia = request.POST.get('codigo_ibge_residencia')
	rua_residencia = request.POST.get('rua_residencia')
	numero_residencia = request.POST.get('numero_residencia')
	complemento_residencia = request.POST.get('complemento_residencia')
	distrito_residencia = request.POST.get('distrito_residencia')
	ponto_referencia_residencia = request.POST.get('ponto_referencia_residencia')
	telefone_residencia = request.POST.get('telefone_residencia')
	zona_residencia = request.POST.get('zona_residencia')
	pais_residencia = request.POST.get('pais_residente_fora_pais')
	
	#Antecedentes Epidemiologicos
	data_investigacao_cap = request.POST.get('data_investigacao')
	if data_investigacao_cap == '' or data_investigacao_cap == None:
		data_investigacao = None
	else:
		data_investigacao = datetime.strptime(data_investigacao_cap, '%Y-%m-%d').date()


	ocupacao = request.POST.get('ocupacao')
	ambientes_frequentados = request.POST.getlist('ambientes_frequentados')
	animais_que_teve_contato = request.POST.getlist('animais_que_teve_contato')
	natureza_contato_animais = request.POST.getlist('natureza_contato_animais')
	relacao_animal_doente = request.POST.getlist('relacao_animal_doente')
	exerce_atividade_contato_plantas = request.POST.get('exerc_ativ_contato_plantas')
	historico_contato_material = request.POST.get('lesao_manuseio')
	
	#dados clínicos
	presenca_lesao_pele = request.POST.get('presenca_lesao_pele')
	natureza_lesao = request.POST.getlist('natureza_lesao')
	natureza_lesao_outro = request.POST.get('natureza_lesao_outros')
	local_lesao = request.POST.getlist('local_lesao')
	local_lesao_outro = request.POST.get('local_lesao_outros')
	diagnostico_forma_extrac_doenca = request.POST.get('diagnostico_extracutaneo')
	localizacao_forma_extrac_doenca = request.POST.get('local_extra_cutanea')
	
	#Dados Laboratoriais
	houve_coleta_material = request.POST.get('coleta_exame_labo_sim')
	
	data_coleta1 = request.POST.get('data_coleta_mat_exame1')
	if data_coleta1 == '' or data_coleta1 == None:
		data_coleta1 = None
		numero_gal1 = None
	else:
		data_coleta1 = datetime.strptime(data_coleta1, '%Y-%m-%d').date()
		numero_gal1 = request.POST.get('numero_gal1')

	data_coleta2 = request.POST.get('data_coleta_mat_exame2')
	if data_coleta2 == '' or data_coleta2 == None:
		data_coleta2 = None
		numero_gal2 = None
	else:
		data_coleta2 = datetime.strptime(data_coleta2, '%Y-%m-%d').date()
		numero_gal2 = request.POST.get('numero_gal2')

	data_coleta3 = request.POST.get('data_coleta_mat_exame3')
	if data_coleta2 == '' or data_coleta2 == None:
		data_coleta2 = None
		numero_gal2 = None
	else:
		data_coleta2 = datetime.strptime(data_coleta2, '%Y-%m-%d').date()
		numero_gal3 = request.POST.get('numero_gal3')
	
	resultado_isolamento = request.POST.get('resultado_isolamento')
	agente = request.POST.get('agente_isolamento')
	histopatologia = request.POST.get('histopatologia')
	
	data_exame1_cap = request.POST.get('data_outros_exames_1')
	if data_exame1_cap == '' or data_exame1_cap == None:
		data_resultado_exame1 = None
	else:
		data_resultado_exame1 = datetime.strptime(data_exame1_cap, '%Y-%m-%d').date()
	

	descricao_exame_1 = request.POST.get('descricao_outros_exames_1')
	resultado_exame1 = request.POST.get('resultado_outros_exames_1')
	
	data_exame2_cap = request.POST.get('data_outros_exames_2')
	if data_exame2_cap == '' or data_exame2_cap == None:
		data_resultado_exame2 = None
	else:
		data_resultado_exame2 = datetime.strptime(data_exame2_cap, '%Y-%m-%d').date()

	
	descricao_exame_2 = request.POST.get('descricao_outros_exames_2')
	resultado_exame2 = request.POST.get('resultado_outros_exames_2')
	
	data_exame3_cap = request.POST.get('data_outros_exames_3')
	if data_exame3_cap == '' or data_exame3_cap == None:
		data_resultado_exame3 = None
	else:
		data_resultado_exame3 = datetime.strptime(data_exame3_cap, '%Y-%m-%d').date()
		
	
	descricao_exame_3 = request.POST.get('descricao_outros_exames_3')
	resultado_exame3 = request.POST.get('resultado_outros_exames_3')
	
	#tratamento
	data_inicio_tratamento1_cap = request.POST.get('data_inicio_tratamento')
	if data_inicio_tratamento1_cap == '' or data_inicio_tratamento1_cap == None:
		data_inicio_tratamento1 = None		
	else:
		data_inicio_tratamento1 = datetime.strptime(data_inicio_tratamento1_cap, '%Y-%m-%d').date()
	

	droga_administrada1 = request.POST.get('droga_admin_tratamento')
	esquema_terapeutico1 = request.POST.get('esquema_terapeutico')
	
	data_inicio_tratamento2_cap = request.POST.get('data_inicio_tratamento2')
	if data_inicio_tratamento2_cap == '' or data_inicio_tratamento2_cap == None:
		data_inicio_tratamento2 = None
	else:
		data_inicio_tratamento2 = datetime.strptime(data_inicio_tratamento2_cap, '%Y-%m-%d').date()
	
	
	droga_administrada2 = request.POST.get('droga_admin_tratamento2')
	esquema_terapeutico2 = request.POST.get('esquema_terapeutico2')
	
	data_inicio_tratamento3_cap = request.POST.get('data_inicio_tratamento3')
	if data_inicio_tratamento3_cap == '' or data_inicio_tratamento3_cap == None:
		data_inicio_tratamento3 = None
	else:
		data_inicio_tratamento3 = datetime.strptime(data_inicio_tratamento3_cap, '%Y-%m-%d').date()
	

	droga_administrada3 = request.POST.get('droga_admin_tratamento3')
	esquema_terapeutico3 = request.POST.get('esquema_terapeutico3')
	hospitalizacao = request.POST.get('hospitalizado')
	
	data_internacao_cap = request.POST.get('data_internacao')
	if data_internacao_cap == '' or data_internacao_cap == None:
		data_internacao = None
	else:
		data_internacao = datetime.strptime(data_internacao_cap, '%Y-%m-%d').date()
	

	data_da_alta_cap = request.POST.get('data_alta')
	if data_da_alta_cap == '' or data_da_alta_cap == None:
		data_da_alta = None
	else:
		data_da_alta = datetime.strptime(data_da_alta_cap, '%Y-%m-%d').date()
	

	uf_hospitalizacao = request.POST.get('uf_internacao')
	municipio_hospitalizacao = request.POST.get('municipio_hospital')
	codigo_ibge_hospitalizacao = request.POST.get('codigo_ibge_municipio_hospitalizacao')
	nome_hospital_hospitalizacao = request.POST.get('nome_hospital_hospitalizacao')
	
	#conclusao
	classificacao_final = request.POST.get('classificacao')
	criterio_confirmacao = request.POST.get('criterio')
	caso_autoctone_municipio_residencia = request.POST.get('autoctone')
	uf_caso_autoctone = request.POST.get('uf_caso_autoctone_municipio')
	pais_caso_autoctone = request.POST.get('pais_autoctone_municipio')
	municipio_caso_autoctone = request.POST.get('municipio_autoctone')
	codigo_ibge_caso_autoctone = request.POST.get('codigo_ibge_municipio_autoctone')
	distrito_caso_autoctone = request.POST.get('distrito_autoctone')
	bairro_caso_autoctone = request.POST.get('bairro_autoctone')
	area_provavel_infeccao_caso_autoctone = request.POST.get('area_provavel_infeccao')
	ambiente_infeccao_caso_autoctone = request.POST.get('ambiente_infeccao_autoctone')
	doenca_rel_trabalho_caso_autoctone = request.POST.get('doenca_rel_trabalho_autoctone')
	evolucao_caso = request.POST.get('evolucao_caso_autoctone')
	
	data_obito_cap = request.POST.get('data_obito')
	if data_obito_cap == '' or data_obito_cap == None:
		data_obito = None
	else:
		data_obito = datetime.strptime(data_obito_cap, '%Y-%m-%d').date()
	

	data_encerramento_cap = request.POST.get('data_encerramento')
	if data_encerramento_cap == '' or data_encerramento_cap == None:
		data_encerramento = None		
	else:
		data_encerramento = datetime.strptime(data_encerramento_cap, '%Y-%m-%d').date()
	
	
	#observação
	observacao = request.POST.get('observacao')
	
	#investigador
	nome_investigador = request.POST.get('nome_investigador')
	funcao_investigador = request.POST.get('funcao_investigador')
	email_investigador = request.POST.get('email_investigador')
	telefone_investigador = request.POST.get('telefone_investigador')
	conselho_classe_investigador = request.POST.get('conselho_classe_investigador')

	registro = CasoEsporotricose.objects.create(
		responsavel_pelas_informacoes = responsavel_pelas_informacoes,
		tipo_notificacao = tipo_notificacao,
		agravo_doenca = agravo_doenca,
		codigo_cib10 = codigo_cib10,
		data_notificacao = data_notificacao,
		estado = estado,
		municipio = municipio,
		gerencia = gerencia,
		codigo_ibge = codigo_ibge,
		data_primeiros_sintomas = data_primeiros_sintomas,
		unidade_saude = unidade_saude,
		unidade_saude_outro = unidade_saude_outro,
		nome_paciente = nome_paciente,
		data_nascimento_paciente = data_nascimento_paciente,
		sexo_paciente = sexo_paciente,
		idade_paciente = idade_paciente,
		paciente_gestante = paciente_gestante,
		raca_paciente = raca_paciente,
		escolaridade_paciente = escolaridade_paciente,
		cartao_sus_paciente = cartao_sus_paciente,
		nome_mae_paciente = nome_mae_paciente,
		cep_residencia = cep_residencia,
		uf_residencia = uf_residencia,
		municipio_residencia = municipio_residencia,
		bairro_residencia = bairro_residencia,
		codigo_ibge_residencia = codigo_ibge_residencia,
		rua_residencia = rua_residencia,
		numero_residencia = numero_residencia,
		complemento_residencia = complemento_residencia,
		distrito_residencia = distrito_residencia,
		ponto_referencia_residencia = ponto_referencia_residencia,
		telefone_residencia = telefone_residencia,
		zona_residencia = zona_residencia,
		pais_residencia = pais_residencia,
		data_investigacao = data_investigacao,
		ocupacao = ocupacao,
		ambientes_frequentados = ambientes_frequentados,
		animais_que_teve_contato = animais_que_teve_contato,
		natureza_contato_animais = natureza_contato_animais,
		relacao_animal_doente = relacao_animal_doente,
		exerce_atividade_contato_plantas = exerce_atividade_contato_plantas,
		historico_contato_material = historico_contato_material,
		presenca_lesao_pele = presenca_lesao_pele,
		natureza_lesao = natureza_lesao,
		natureza_lesao_outro = natureza_lesao_outro,
		local_lesao = local_lesao,
		local_lesao_outro = local_lesao_outro,
		diagnostico_forma_extrac_doenca = diagnostico_forma_extrac_doenca,
		localizacao_forma_extrac_doenca = localizacao_forma_extrac_doenca,
		houve_coleta_material = houve_coleta_material,
		data_coleta1 = data_coleta1,
		numero_gal1 = numero_gal1,
		data_coleta2 = data_coleta2,
		numero_gal2 = numero_gal2,
		data_coleta3 = data_coleta3,
		numero_gal3 = numero_gal3,
		resultado_isolamento = resultado_isolamento,
		agente = agente,
		histopatologia = histopatologia,
		data_resultado_exame1 = data_resultado_exame1,
		descricao_exame_1 = descricao_exame_1,
		resultado_exame1 = resultado_exame1,
		data_resultado_exame2 = data_resultado_exame2,
		descricao_exame_2 = descricao_exame_2,
		resultado_exame2 = resultado_exame2,
		data_resultado_exame3 = data_resultado_exame3,
		descricao_exame_3 = descricao_exame_3,
		resultado_exame3 = resultado_exame3,
		data_inicio_tratamento1 = data_inicio_tratamento1,
		droga_administrada1 = droga_administrada1,
		esquema_terapeutico1 = esquema_terapeutico1,
		data_inicio_tratamento2 = data_inicio_tratamento2,
		droga_administrada2 = droga_administrada2,
		esquema_terapeutico2 = esquema_terapeutico2,
		data_inicio_tratamento3 = data_inicio_tratamento3,
		droga_administrada3 = droga_administrada3,
		esquema_terapeutico3 = esquema_terapeutico3,
		hospitalizacao = hospitalizacao,
		data_internacao = data_internacao,
		data_da_alta = data_da_alta,
		uf_hospitalizacao = uf_hospitalizacao,
		municipio_hospitalizacao = municipio_hospitalizacao,
		codigo_ibge_hospitalizacao = codigo_ibge_hospitalizacao,
		nome_hospital_hospitalizacao = nome_hospital_hospitalizacao,
		classificacao_final = classificacao_final,
		criterio_confirmacao = criterio_confirmacao,
		caso_autoctone_municipio_residencia = caso_autoctone_municipio_residencia,
		uf_caso_autoctone = uf_caso_autoctone,
		pais_caso_autoctone = pais_caso_autoctone,
		municipio_caso_autoctone = municipio_caso_autoctone,
		codigo_ibge_caso_autoctone = codigo_ibge_caso_autoctone,
		distrito_caso_autoctone = distrito_caso_autoctone,
		bairro_caso_autoctone = bairro_caso_autoctone,
		area_provavel_infeccao_caso_autoctone = area_provavel_infeccao_caso_autoctone,
		ambiente_infeccao_caso_autoctone = ambiente_infeccao_caso_autoctone,
		doenca_rel_trabalho_caso_autoctone = doenca_rel_trabalho_caso_autoctone,
		evolucao_caso = evolucao_caso,
		data_obito = data_obito,
		data_encerramento = data_encerramento,
		observacao = observacao,
		nome_investigador = nome_investigador,
		funcao_investigador = funcao_investigador,
		email_investigador = email_investigador,
		telefone_investigador = telefone_investigador,
		conselho_classe_investigador = conselho_classe_investigador

		)


	return redirect('my_datas')

@login_required(login_url='/login/')
def caso_esporotricose_edit(request, id):
	caso = CasoEsporotricose.objects.get(id=id)
	estados = Estado.objects.all().order_by('nome')
	municipios = Municipio.objects.all().order_by('nome')
	unidades_saude = []
	codigos_ibge = []
	print(caso.data_coleta)
	caso.data_notificacao = datetime.strftime(caso.data_notificacao, '%Y-%m-%d')
	caso.data_primeiros_sintomas = datetime.strftime(caso.data_primeiros_sintomas, '%Y-%m-%d')
	caso.data_nascimento_paciente = datetime.strftime(caso.data_nascimento_paciente, '%Y-%m-%d')
	if caso.data_resultado_exame1 != None:
		caso.data_resultado_exame1 = datetime.strftime(caso.data_resultado_exame1, '%Y-%m-%d')
	if caso.data_resultado_exame2 != None:
		caso.data_resultado_exame2 = datetime.strftime(caso.data_resultado_exame2, '%Y-%m-%d')
	if caso.data_resultado_exame3 != None:
		caso.data_resultado_exame3 = datetime.strftime(caso.data_resultado_exame3, '%Y-%m-%d')
	if caso.data_coleta1 != None:
		caso.data_coleta1 = datetime.strftime(caso.data_coleta1, '%Y-%m-%d')
	if caso.data_coleta2 != None:
		caso.data_coleta2 = datetime.strftime(caso.data_coleta2, '%Y-%m-%d')
	if caso.data_coleta3 != None:
		caso.data_coleta3 = datetime.strftime(caso.data_coleta3, '%Y-%m-%d')
	if caso.data_investigacao != None:
		caso.data_investigacao = datetime.strftime(caso.data_investigacao, '%Y-%m-%d')
	return render(request, 'caso_esporotricose_edit.html', {'form':caso, 'municipios':municipios, 'unidades_saude':unidades_saude, 
		'codigos_ibge':codigos_ibge, 'estados':estados})

@login_required(login_url='/login/')
def set_caso_esporotricose_edit(request, id):
	print("entrou no set caso esporotricose")
	responsavel_pelas_informacoes = request.user

	#Dados Gerais
	tipo_notificacao = request.POST.get('tipo_notificacao')
	agravo_doenca = request.POST.get('agravo_doenca')
	codigo_cib10 = request.POST.get('codigo_cid')
	
	data_notificacao_cap = request.POST.get('data_notificacao')
	
	if data_notificacao_cap == '' or data_notificacao_cap == None:
		data_notificacao = None
	else:
		data_notificacao = datetime.strptime(data_notificacao_cap, '%Y-%m-%d').date()

	
	estado = request.POST.get('uf_notificacao')
	
	municipio_cap = request.POST.get('municipio_notificacao')
	if municipio_cap == '' or municipio_cap == None:
		municipio = None
	else:
		municipio = int(municipio_cap)

	municipio_id = municipio
	municipio_ = Municipio.objects.get(id=municipio_id)


	gerencia = municipio_.gerencia

	codigo_ibge = request.POST.get('codigo_ibge_dados_gerais')
	
	data_primeiros_sintomas_cap = request.POST.get('data_primeiros_sintomas')
	if data_primeiros_sintomas_cap == '' or data_primeiros_sintomas_cap == None:
		data_primeiros_sintomas = None
	else:
		data_primeiros_sintomas = datetime.strptime(data_primeiros_sintomas_cap, '%Y-%m-%d').date()

	
	unidade_saude = request.POST.get('unidade_saude')
	unidade_saude_outro = request.POST.get('unidade_saude_outro')
	
	#notificação individual
	nome_paciente = request.POST.get('nome_paciente').upper()
	
	data_nascimento_paciente_cap = request.POST.get('data_nasc')
	if data_nascimento_paciente_cap == '' or data_nascimento_paciente_cap == None:
		data_nascimento_paciente = None
	else:
		data_nascimento_paciente = datetime.strptime(data_nascimento_paciente_cap, '%Y-%m-%d').date()

	sexo_paciente = request.POST.get('sexo')
	
	idade_paciente_cap = request.POST.get('result')
	if idade_paciente_cap == '' or idade_paciente_cap == None:
		idade_paciente = None
	else:
		idade_paciente = int(idade_paciente_cap)

	paciente_gestante = request.POST.get('gestacao')
	raca_paciente = request.POST.get('raca')
	escolaridade_paciente = request.POST.get('escolaridade')
	cartao_sus_paciente = request.POST.get('cartao_sus')
	nome_mae_paciente = request.POST.get('nome_mae').upper()
	
	#Dados Residencia
	cep_residencia = request.POST.get('cep_residencia')
	uf_residencia = request.POST.get('uf_residencia')
	municipio_residencia = request.POST.get('cidade_residencia')
	bairro_residencia = request.POST.get('bairro_residencia')
	codigo_ibge_residencia = request.POST.get('codigo_ibge_residencia')
	rua_residencia = request.POST.get('rua_residencia')
	numero_residencia = request.POST.get('numero_residencia')
	complemento_residencia = request.POST.get('complemento_residencia')
	distrito_residencia = request.POST.get('distrito_residencia')
	ponto_referencia_residencia = request.POST.get('ponto_referencia_residencia')
	telefone_residencia = request.POST.get('telefone_residencia')
	zona_residencia = request.POST.get('zona_residencia')
	pais_residencia = request.POST.get('pais_residente_fora_pais')
	
	#Antecedentes Epidemiologicos
	data_investigacao_cap = request.POST.get('data_investigacao')
	if data_investigacao_cap == '' or data_investigacao_cap == None:
		data_investigacao = None
	else:
		data_investigacao = datetime.strptime(data_investigacao_cap, '%Y-%m-%d').date()


	ocupacao = request.POST.get('ocupacao')
	ambientes_frequentados = request.POST.getlist('ambientes_frequentados')
	animais_que_teve_contato = request.POST.getlist('animais_que_teve_contato')
	natureza_contato_animais = request.POST.getlist('natureza_contato_animais')
	relacao_animal_doente = request.POST.getlist('relacao_animal_doente')
	exerce_atividade_contato_plantas = request.POST.get('exerc_ativ_contato_plantas')
	historico_contato_material = request.POST.get('lesao_manuseio')
	
	#dados clínicos
	presenca_lesao_pele = request.POST.get('presenca_lesao_pele')
	natureza_lesao = request.POST.getlist('natureza_lesao')
	natureza_lesao_outro = request.POST.get('natureza_lesao_outros')
	local_lesao = request.POST.getlist('local_lesao')
	local_lesao_outro = request.POST.get('local_lesao_outros')
	diagnostico_forma_extrac_doenca = request.POST.get('diagnostico_extracutaneo')
	localizacao_forma_extrac_doenca = request.POST.get('local_extra_cutanea')
	
	#Dados Laboratoriais
	houve_coleta_material = request.POST.get('coleta_exame_labo_sim')
	
	data_coleta1 = request.POST.get('data_coleta_mat_exame1')
	if data_coleta1 == '' or data_coleta1 == None:
		data_coleta1 = None
		numero_gal1 = None
	else:
		data_coleta1 = datetime.strptime(data_coleta1, '%Y-%m-%d').date()
		numero_gal1 = request.POST.get('numero_gal1')

	data_coleta2 = request.POST.get('data_coleta_mat_exame2')
	if data_coleta2 == '' or data_coleta2 == None:
		data_coleta2 = None
		numero_gal2 = None
	else:
		data_coleta2 = datetime.strptime(data_coleta2, '%Y-%m-%d').date()
		numero_gal2 = request.POST.get('numero_gal2')

	data_coleta3 = request.POST.get('data_coleta_mat_exame3')
	if data_coleta2 == '' or data_coleta2 == None:
		data_coleta2 = None
		numero_gal2 = None
	else:
		data_coleta2 = datetime.strptime(data_coleta2, '%Y-%m-%d').date()
		numero_gal3 = request.POST.get('numero_gal3')
	
	resultado_isolamento = request.POST.get('resultado_isolamento')
	agente = request.POST.get('agente_isolamento')
	histopatologia = request.POST.get('histopatologia')
	
	data_exame1_cap = request.POST.get('data_outros_exames_1')
	if data_exame1_cap == '' or data_exame1_cap == None:
		data_resultado_exame1 = None
	else:
		data_resultado_exame1 = datetime.strptime(data_exame1_cap, '%Y-%m-%d').date()
	

	descricao_exame_1 = request.POST.get('descricao_outros_exames_1')
	resultado_exame1 = request.POST.get('resultado_outros_exames_1')
	
	data_exame2_cap = request.POST.get('data_outros_exames_2')
	if data_exame2_cap == '' or data_exame2_cap == None:
		data_resultado_exame2 = None
	else:
		data_resultado_exame2 = datetime.strptime(data_exame2_cap, '%Y-%m-%d').date()

	
	descricao_exame_2 = request.POST.get('descricao_outros_exames_2')
	resultado_exame2 = request.POST.get('resultado_outros_exames_2')
	
	data_exame3_cap = request.POST.get('data_outros_exames_3')
	if data_exame3_cap == '' or data_exame3_cap == None:
		data_resultado_exame3 = None
	else:
		data_resultado_exame3 = datetime.strptime(data_exame3_cap, '%Y-%m-%d').date()
		
	
	descricao_exame_3 = request.POST.get('descricao_outros_exames_3')
	resultado_exame3 = request.POST.get('resultado_outros_exames_3')
	
	#tratamento
	data_inicio_tratamento1_cap = request.POST.get('data_inicio_tratamento')
	if data_inicio_tratamento1_cap == '' or data_inicio_tratamento1_cap == None:
		data_inicio_tratamento1 = None		
	else:
		data_inicio_tratamento1 = datetime.strptime(data_inicio_tratamento1_cap, '%Y-%m-%d').date()
	

	droga_administrada1 = request.POST.get('droga_admin_tratamento')
	esquema_terapeutico1 = request.POST.get('esquema_terapeutico')
	
	data_inicio_tratamento2_cap = request.POST.get('data_inicio_tratamento2')
	if data_inicio_tratamento2_cap == '' or data_inicio_tratamento2_cap == None:
		data_inicio_tratamento2 = None
	else:
		data_inicio_tratamento2 = datetime.strptime(data_inicio_tratamento2_cap, '%Y-%m-%d').date()
	
	
	droga_administrada2 = request.POST.get('droga_admin_tratamento2')
	esquema_terapeutico2 = request.POST.get('esquema_terapeutico2')
	
	data_inicio_tratamento3_cap = request.POST.get('data_inicio_tratamento3')
	if data_inicio_tratamento3_cap == '' or data_inicio_tratamento3_cap == None:
		data_inicio_tratamento3 = None
	else:
		data_inicio_tratamento3 = datetime.strptime(data_inicio_tratamento3_cap, '%Y-%m-%d').date()
	

	droga_administrada3 = request.POST.get('droga_admin_tratamento3')
	esquema_terapeutico3 = request.POST.get('esquema_terapeutico3')
	hospitalizacao = request.POST.get('hospitalizado')
	
	data_internacao_cap = request.POST.get('data_internacao')
	if data_internacao_cap == '' or data_internacao_cap == None:
		data_internacao = None
	else:
		data_internacao = datetime.strptime(data_internacao_cap, '%Y-%m-%d').date()
	

	data_da_alta_cap = request.POST.get('data_alta')
	if data_da_alta_cap == '' or data_da_alta_cap == None:
		data_da_alta = None
	else:
		data_da_alta = datetime.strptime(data_da_alta_cap, '%Y-%m-%d').date()
	

	uf_hospitalizacao = request.POST.get('uf_internacao')
	municipio_hospitalizacao = request.POST.get('municipio_hospital')
	codigo_ibge_hospitalizacao = request.POST.get('codigo_ibge_municipio_hospitalizacao')
	nome_hospital_hospitalizacao = request.POST.get('nome_hospital_hospitalizacao')
	
	#conclusao
	classificacao_final = request.POST.get('classificacao')
	criterio_confirmacao = request.POST.get('criterio')
	caso_autoctone_municipio_residencia = request.POST.get('autoctone')
	uf_caso_autoctone = request.POST.get('uf_caso_autoctone_municipio')
	pais_caso_autoctone = request.POST.get('pais_autoctone_municipio')
	municipio_caso_autoctone = request.POST.get('municipio_autoctone')
	codigo_ibge_caso_autoctone = request.POST.get('codigo_ibge_municipio_autoctone')
	distrito_caso_autoctone = request.POST.get('distrito_autoctone')
	bairro_caso_autoctone = request.POST.get('bairro_autoctone')
	area_provavel_infeccao_caso_autoctone = request.POST.get('area_provavel_infeccao')
	ambiente_infeccao_caso_autoctone = request.POST.get('ambiente_infeccao_autoctone')
	doenca_rel_trabalho_caso_autoctone = request.POST.get('doenca_rel_trabalho_autoctone')
	evolucao_caso = request.POST.get('evolucao_caso_autoctone')
	
	data_obito_cap = request.POST.get('data_obito')
	if data_obito_cap == '' or data_obito_cap == None:
		data_obito = None
	else:
		data_obito = datetime.strptime(data_obito_cap, '%Y-%m-%d').date()
	

	data_encerramento_cap = request.POST.get('data_encerramento')
	if data_encerramento_cap == '' or data_encerramento_cap == None:
		data_encerramento = None		
	else:
		data_encerramento = datetime.strptime(data_encerramento_cap, '%Y-%m-%d').date()
	
	
	#observação
	observacao = request.POST.get('observacao')
	
	#investigador
	nome_investigador = request.POST.get('nome_investigador')
	funcao_investigador = request.POST.get('funcao_investigador')
	email_investigador = request.POST.get('email_investigador')
	telefone_investigador = request.POST.get('telefone_investigador')
	conselho_classe_investigador = request.POST.get('conselho_classe_investigador')

	CasoEsporotricose.objects.update(
		responsavel_pelas_informacoes = responsavel_pelas_informacoes,
		tipo_notificacao = tipo_notificacao,
		agravo_doenca = agravo_doenca,
		codigo_cib10 = codigo_cib10,
		data_notificacao = data_notificacao,
		estado = estado,
		municipio = municipio,
		gerencia = gerencia,
		codigo_ibge = codigo_ibge,
		data_primeiros_sintomas = data_primeiros_sintomas,
		unidade_saude = unidade_saude,
		unidade_saude_outro = unidade_saude_outro,
		nome_paciente = nome_paciente,
		data_nascimento_paciente = data_nascimento_paciente,
		sexo_paciente = sexo_paciente,
		idade_paciente = idade_paciente,
		paciente_gestante = paciente_gestante,
		raca_paciente = raca_paciente,
		escolaridade_paciente = escolaridade_paciente,
		cartao_sus_paciente = cartao_sus_paciente,
		nome_mae_paciente = nome_mae_paciente,
		cep_residencia = cep_residencia,
		uf_residencia = uf_residencia,
		municipio_residencia = municipio_residencia,
		bairro_residencia = bairro_residencia,
		codigo_ibge_residencia = codigo_ibge_residencia,
		rua_residencia = rua_residencia,
		numero_residencia = numero_residencia,
		complemento_residencia = complemento_residencia,
		distrito_residencia = distrito_residencia,
		ponto_referencia_residencia = ponto_referencia_residencia,
		telefone_residencia = telefone_residencia,
		zona_residencia = zona_residencia,
		pais_residencia = pais_residencia,
		data_investigacao = data_investigacao,
		ocupacao = ocupacao,
		ambientes_frequentados = ambientes_frequentados,
		animais_que_teve_contato = animais_que_teve_contato,
		natureza_contato_animais = natureza_contato_animais,
		relacao_animal_doente = relacao_animal_doente,
		exerce_atividade_contato_plantas = exerce_atividade_contato_plantas,
		historico_contato_material = historico_contato_material,
		presenca_lesao_pele = presenca_lesao_pele,
		natureza_lesao = natureza_lesao,
		natureza_lesao_outro = natureza_lesao_outro,
		local_lesao = local_lesao,
		local_lesao_outro = local_lesao_outro,
		diagnostico_forma_extrac_doenca = diagnostico_forma_extrac_doenca,
		localizacao_forma_extrac_doenca = localizacao_forma_extrac_doenca,
		houve_coleta_material = houve_coleta_material,
		data_coleta1 = data_coleta1,
		numero_gal1 = numero_gal1,
		data_coleta2 = data_coleta2,
		numero_gal2 = numero_gal2,
		data_coleta3 = data_coleta3,
		numero_gal3 = numero_gal3,
		resultado_isolamento = resultado_isolamento,
		agente = agente,
		histopatologia = histopatologia,
		data_resultado_exame1 = data_resultado_exame1,
		descricao_exame_1 = descricao_exame_1,
		resultado_exame1 = resultado_exame1,
		data_resultado_exame2 = data_resultado_exame2,
		descricao_exame_2 = descricao_exame_2,
		resultado_exame2 = resultado_exame2,
		data_resultado_exame3 = data_resultado_exame3,
		descricao_exame_3 = descricao_exame_3,
		resultado_exame3 = resultado_exame3,
		data_inicio_tratamento1 = data_inicio_tratamento1,
		droga_administrada1 = droga_administrada1,
		esquema_terapeutico1 = esquema_terapeutico1,
		data_inicio_tratamento2 = data_inicio_tratamento2,
		droga_administrada2 = droga_administrada2,
		esquema_terapeutico2 = esquema_terapeutico2,
		data_inicio_tratamento3 = data_inicio_tratamento3,
		droga_administrada3 = droga_administrada3,
		esquema_terapeutico3 = esquema_terapeutico3,
		hospitalizacao = hospitalizacao,
		data_internacao = data_internacao,
		data_da_alta = data_da_alta,
		uf_hospitalizacao = uf_hospitalizacao,
		municipio_hospitalizacao = municipio_hospitalizacao,
		codigo_ibge_hospitalizacao = codigo_ibge_hospitalizacao,
		nome_hospital_hospitalizacao = nome_hospital_hospitalizacao,
		classificacao_final = classificacao_final,
		criterio_confirmacao = criterio_confirmacao,
		caso_autoctone_municipio_residencia = caso_autoctone_municipio_residencia,
		uf_caso_autoctone = uf_caso_autoctone,
		pais_caso_autoctone = pais_caso_autoctone,
		municipio_caso_autoctone = municipio_caso_autoctone,
		codigo_ibge_caso_autoctone = codigo_ibge_caso_autoctone,
		distrito_caso_autoctone = distrito_caso_autoctone,
		bairro_caso_autoctone = bairro_caso_autoctone,
		area_provavel_infeccao_caso_autoctone = area_provavel_infeccao_caso_autoctone,
		ambiente_infeccao_caso_autoctone = ambiente_infeccao_caso_autoctone,
		doenca_rel_trabalho_caso_autoctone = doenca_rel_trabalho_caso_autoctone,
		evolucao_caso = evolucao_caso,
		data_obito = data_obito,
		data_encerramento = data_encerramento,
		observacao = observacao,
		nome_investigador = nome_investigador,
		funcao_investigador = funcao_investigador,
		email_investigador = email_investigador,
		telefone_investigador = telefone_investigador,
		conselho_classe_investigador = conselho_classe_investigador

		)


	return redirect('my_datas')