from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

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


def set_login_page(request):
	return redirect('index')


def index(request):
	return render(request, 'index.html')


def main(request):
	return render(request, 'main.html')


def all_forms(request):
	return render(request, 'all_forms.html')


def informar_dados_ficha(request):
	return render(request, 'informar_dados_ficha.html')

def localizar_paciente_nome(request):
	return render(request, 'localizar_paciente_nome.html')

def set_localizar_paciente_nome(request):
	return render(request, 'resultado_search_caso_nome.html')

def caso_view(request):
	return render(request, 'caso_view.html')

def caso_view_detail(request):
	return render(request, 'caso_view_detail.html')

def caso_esporotricose_create(request):
	return render(request, 'caso_esporotricose_create.html')


def set_caso_esporotricose_create(request):
	responsavel_pelas_informacoes = request.user

	#Dados Gerais
	tipo_notificacao = request.POST.get('tipo_notificacao')
	agravo_doenca = request.POST.get('agravo_doenca')
	codigo_cib10 = request.POST.get('codigo_cib')
	data_notificacao = request.POST.get('data_notificacao')
	estado = request.POST.get('uf_notificacao')
	municipio = request.POST.get('municipio_notificacao')
	codigo_ibge = request.POST.get('codigo_ibge_dados_gerais')
	data_primeiros_sintomas = request.POST.get('data_primeiros_sintomas')
	unidade_saude = request.POST.get('unidade_saude')
	
	#notificação individual
	nome_paciente = request.POST.get('nome_paciente')
	data_nascimento_paciente = request.POST.get('data_nasc')
	sexo_paciente = request.POST.get('sexo')
	idade_paciente = request.POST.get('result')
	paciente_gestante = request.POST.get('gestacao')
	raca_paciente = request.POST.get('raca')
	escolaridade_paciente = request.POST.get('escolaridade')
	cantao_sus_paciente = request.POST.get('cartao_sus')
	nome_mae_paciente = request.POST.get('nome_mae')
	
	#Dados Residencia
	cep_residencia = request.POST.get('')
	uf_residencia = request.POST.get('')
	municipio_residencia = request.POST.get('')
	bairro_residencia = request.POST.get('')
	codigo_ibge_residencia = request.POST.get('')
	rua_residencia = request.POST.get('')
	numero_residencia = request.POST.get('')
	complemento_residencia = request.POST.get('')
	distrito_residencia = request.POST.get('')
	ponto_referencia_residencia = request.POST.get('')
	telefone_residencia = request.POST.get('')
	zona_residencia = request.POST.get('')
	pais_residencia = request.POST.get('')
	
	#Antecedentes Epidemiologicos
	data_investigacao = request.POST.get('')
	ocupacao = request.POST.get('')
	ambientes_frequentados = request.POST.getlist('')
	animais_que_teve_contato = request.POST.getlist('')
	natureza_contato_animais = request.POST.getlist('')
	relacao_animal_doente = request.POST.getlist('')
	exerce_atividade_contato_plantas = request.POST.get('')
	historico_contato_material = request.POST.get('')
	
	#dados clínicos
	presenca_lesao_pele = request.POST.get('')
	natureza_lesao = request.POST.getlist('')
	local_lesao = request.POST.getlist('')
	diagnostico_forma_extrac_doenca = request.POST.get('')
	localizacao_forma_extrac_doenca = request.POST.get('')
	
	#Dados Laboratoriais
	houve_coleta_material = request.POST.get('')
	data_coleta = request.POST.get('')
	resultado_isolamento = request.POST.get('')
	agente = request.POST.get('')
	histopatologia = request.POST.get('')
	data_exame1 = request.POST.get('')
	descricao_exame_1 = request.POST.get('')
	resultado_exame1 = request.POST.get('')
	data_exame2 = request.POST.get('')
	descricao_exame_2 = request.POST.get('')
	resultado_exame2 = request.POST.get('')
	data_exame3 = request.POST.get('')
	descricao_exame_3 = request.POST.get('')
	resultado_exame3 = request.POST.get('')
	
	#tratamento
	data_inicio_tratamento1 = request.POST.get('')
	droga_administrada1 = request.POST.get('')
	esquema_terapeutico1 = request.POST.get('')
	data_inicio_tratamento2 = request.POST.get('')
	droga_administrada2 = request.POST.get('')
	esquema_terapeutico2 = request.POST.get('')
	data_inicio_tratamento3 = request.POST.get('')
	droga_administrada3 = request.POST.get('')
	esquema_terapeutico3 = request.POST.get('')
	hospitalizacao = request.POST.get('')
	data_internacao = request.POST.get('')
	data_da_alta = request.POST.get('')
	uf_hospitalizacao = request.POST.get('')
	municipio_hospitalizacao = request.POST.get('')
	codigo_ibge_hospitalizacao = request.POST.get('')
	nome_hospital_hospitalizacao = request.POST.get('')
	
	#conclusao
	classificacao_final = request.POST.get('')
	criterio_confirmacao = request.POST.get('')
	caso_autoctone_municipio_residencia = request.POST.get('')
	uf_caso_autoctone = request.POST.get('')
	pais_caso_autoctone = request.POST.get('')
	municipio_caso_autoctone = request.POST.get('')
	codigo_ibge_caso_autoctone = request.POST.get('')
	distrito_caso_autoctone = request.POST.get('')
	bairro_caso_autoctone = request.POST.get('')
	area_provavel_infeccao_caso_autoctone = request.POST.get('')
	ambiente_infeccao_caso_autoctone = request.POST.get('')
	doenca_rel_trabalho_caso_autoctone = request.POST.get('')
	evolucao_caso = request.POST.get('')
	data_obito = request.POST.get('')
	data_encerramento = request.POST.get('')
	
	#observação
	observacao = request.POST.get('')
	
	#investigador
	nome_investigador = request.POST.get('')
	funcao_investigador = request.POST.get('')
	email_investigador = request.POST.get('')
	telefone_investigador = request.POST.get('')
	conselho_classe_investigador = request.POST.get('')

	return redirect('index')