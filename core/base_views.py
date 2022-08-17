from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.db.models import Q

from io import BytesIO
import pandas as pd
import json

from _esporotricose_humana.models import CasoEsporotricose
from _acidente_transito.models import Acidente
from .models import *



# Lista de todos os agravos.
AGRAVOS = ['esp-hum', 'act']

# KEY: AGRAVO URL | VALUE: DADOS DO AGRAVO
AGRAVOS_DADOS = {
    'esp-hum':CasoEsporotricose.objects.all(),
    'act':Acidente.objects.all(),
}

# Funcoes SES
FUNCOES_SES = ["admin", "gerencia_executiva", "gerencia_operacional","chefia_nucleo", "area_tecnica"]


# Função responsável por retornar a pagina principal.
@login_required(login_url='/login/')
def principal(request):	
	return render(request, 'principal.html')


# Função responsável por retornar a pagina dos dados do usuário.
@login_required(login_url='/login/')
def dados_user(request):
	return render(request, 'dados_user.html')


# Função responsável por retornar as notificações referente a pesquisa.
def my_data(dados):
    
    # Identificando o agravo pela url.
    agravo_url = str(dados.path).split('/')[1]
    
    # Registros da doença escolhida.
    registros =  AGRAVOS_DADOS[agravo_url]
    
	# Pegando os dados de municipio.
    municipios = Municipio.objects.all()
	
    # Filtrando dados por função do usuário.
    if dados.user.funcao == 'gerencia_regional':        
        user_gerencia_regional = Municipio.objects.get(id=dados.user.municipio_id).gerencia_id
        registros = registros.filter(gerencia_id=user_gerencia_regional)

    elif dados.user.funcao == 'municipal':
        
        user_municipio_id = dados.user.municipio_id
        user_id = dados.user.id
        user_municipio_nome = str(Municipio.objects.filter(id=user_municipio_id)[0])
        user_municipio_nome_upper = str(Municipio.objects.filter(id=user_municipio_id)[0]).upper()
        
        registros = registros.filter(
			Q(municipio_residencia=user_municipio_id) | 
			Q(municipio_residencia=user_municipio_nome) | 
			Q(municipio_residencia=user_municipio_nome_upper) | 
			Q(responsavel_pelas_informacoes_id=user_id)
			)
        
    elif dados.user.funcao == 'autocadastro':
        autocadastro_id = dados.user.id
        registros = registros.filter(responsavel_pelas_informacoes_id=autocadastro_id)
        
    if agravo_url == 'esp-hum':
        registros = registros.order_by('-data_notificacao').exclude(status_caso='Cancelado')
    else:
        registros = registros.order_by('-id').exclude(status_caso='Cancelado')

    # Criando paginação (DESABILITADO) #
    # paginator = Paginator(registros, 6)
    # page = request.GET.get('page')
    # regs = paginator.get_page(page)    
    
    return {'regs':registros, 'municipios':municipios}
    

# Função responsável por exportar dados.
@login_required(login_url='/login/')
def export_data_excel(request):
    
    # Variaveis de filtro.
    agravo_url = str(request.path).split('/')[1]
    filtro_url = str(request.path).split('/')[2]

    # Nome do arquivo de acordo com a doença.
    file_name = f'notificacoes_{agravo_url}.xlsx'

    # Pegando todos os casos registrados
    casos = AGRAVOS_DADOS[agravo_url]

    # Se for para exportar apenas casos cancelados.
    if filtro_url == 'export_casos_cancelados':
        casos = casos.filter(status_caso='Cancelado')
        file_name = f'notificacoes_canceladas_{agravo_url}.xlsx'

	
    # Filtrando se houver filtro.
    filtro_data_inicio = request.GET.get('filtro_data_inicio')
    filtro_data_fim = request.GET.get('filtro_data_fim')
    filtros_data = [filtro_data_inicio, filtro_data_fim]
    for filtro in filtros_data:
        if filtro == '' or filtro == None:
            filtros_data.remove(filtro)


    # Filtrando datas
    # Se o agravo for esporotricose humana filtrar por data de primeiros sintomas.
    if agravo_url == 'esp-hum':
        if len(filtros_data) == 2:
            casos_filtrados = casos.filter(data_primeiros_sintomas__range=[filtro_data_inicio,filtro_data_fim]).order_by('-id')

        elif len(filtros_data) == 1 and filtros_data[0] != '':
            filtro_unico_dia = filtros_data[0]
            casos_filtrados = casos.filter(data_primeiros_sintomas=filtro_unico_dia).order_by('-id')

        else:
            casos_filtrados = casos.order_by('-id')

    # Se o agravo for acidente de transito filtrar por data de notificacao.
    elif agravo_url == 'act':
        
        if len(filtros_data) == 2:
            casos_filtrados = casos.filter(data_acidente__range=[filtro_data_inicio,filtro_data_fim]).order_by('-id')

        elif len(filtros_data) == 1 and filtros_data[0] != '':
            filtro_unico_dia = filtros_data[0]
            casos_filtrados = casos.filter(data_acidente=filtro_unico_dia).order_by('-id')

        else:
            casos_filtrados = casos.order_by('-id')
        

    # Filtrando o tipo de perfil para limitar os casos.
    if request.user.funcao == 'autocadastro':
        # Perfil Auto-Cadastro
        auto_cadastro_id = request.user.id
        casos_response = casos_filtrados.filter(responsavel_pelas_informacoes_id=auto_cadastro_id).order_by('-id')

    elif request.user.funcao == 'municipal':
        # Perfil Municipal
        user_municipio_id = request.user.municipio_id
        user_municipio_nome = str(Municipio.objects.filter(id=user_municipio_id)[0]).upper()
        casos_response = casos_filtrados.filter(Q(municipio_residencia=user_municipio_id) | 
            Q(municipio_residencia=user_municipio_nome) | Q(responsavel_pelas_informacoes_id=user_municipio_id)).order_by('-id')

    elif request.user.funcao == 'gerencia_regional':
        # Perfil Gerencia Regional
        user_gerencia_regional = Municipio.objects.get(id=request.user.municipio_id).gerencia_id
        casos_response = casos_filtrados.filter(gerencia_id=user_gerencia_regional).order_by('-id')

    else: # Qualquer outro tipo de perfil
        casos_response = casos_filtrados
        
    # Convertendo em dataframe e alterando o campo município.
    try:
        data = list(casos_response.order_by('-id').values())
        df = pd.DataFrame(data)
        if agravo_url == 'esp-hum':
            for i in df['municipio']:            
                try: # Checando se o valor é diferente de NaN
                    i = int(i)
                except:
                    continue
                else: # Buscando no modelo municipio o nome de municipio pelo id e alterando o dataframe
                    municipio = Municipio.objects.get(id=i)
                    df['municipio'] = df['municipio'].replace([i], municipio.nome)

    except Exception as e:
        raise e

    else:
        # Escrevendo o excel e enviando o response.
        with BytesIO() as b:
            
            writer = pd.ExcelWriter(b, engine='openpyxl')
            df.to_excel(writer, sheet_name='Sheet1', index=False)
            writer.save()
            
            filename = file_name
            response = HttpResponse(b.getvalue(),content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=%s' % filename
            
            return response


# Função responsável por cancelar um dado.
@login_required(login_url='/login/')
def cancelar_caso(request, id):

    # Variaveis de filtro.
    agravo_url = str(request.path).split('/')[1]
    
    # Redirecionamento url.
    redirect_url = f'/{agravo_url}/casos_cancelados/'
    
    # Pegando todos os dados.
    agravo = AGRAVOS_DADOS[agravo_url]
    
    # Filtrando pelo id
    registro = agravo.filter(id=id).values()

    # Se já estiver cancelado, habilita novamente.
    if registro[0]['status_caso'] == 'Cancelado':
        agravo.filter(id=id).update(status_caso=None)
    
    # Caso esteja habilitado, cancela o caso.
    else:		
        agravo.filter(id=id).update(status_caso='Cancelado')

    return redirect(redirect_url)


# Função responsável por renderizar a pagina de escolha de agravo para notificar.
@login_required(login_url='/login/')
def all_forms(request):
	
	if request.user.funcao != 'gerencia_regional':
		return render(request, 'all_forms.html')
	else:
		return redirect('principal')


# Função que renderiza a pagina de usuarios.
@csrf_exempt
@login_required(login_url='/login/')
def usuarios(request, id=None):

    if request.user.funcao in FUNCOES_SES: 

        # Renderizando a pagina.
        if request.method == "GET":

            if hierarchy_has_change() or admin_has_change():
                return redirect("/usuarios")            

            agravos = request.user.lista_agravos_permite
            user_hierarquia = request.user.numero_hierarquia
                    
            # Separando os usuários com nivel hierarquico menor que o user.
            usuarios_lista = get_user_model().objects.all().filter(numero_hierarquia__gt=user_hierarquia).order_by('id')
            
            # Filtrando usuários que tem acesso ao agravo que o user gerencia.
            usuarios = []
            for usuario in usuarios_lista:
                
                user_dict = usuario.__dict__
                user_dict['municipio'] = usuario.municipio
                
                # Removendo informações sensíveis.
                del user_dict['password'], user_dict['cpf']

                # Adicionando marcador para o checkbox de agravos permitidos.
                for agravo in usuario.lista_agravos_permite:
                    if agravo in agravos:
                        if agravo == 'esp-hum':
                            user_dict['esp_hum'] = True
                        elif agravo == 'act':
                            user_dict['act'] = True
                
                # Adicionando marcador para o checkbox de solicitaçao de agravos.
                for agravo in usuario.lista_agravos_possivel:
                    if agravo in agravos:
                        if agravo == 'esp-hum':
                            user_dict['esp_hum_solicit'] = True
                        elif agravo == 'act':
                            user_dict['act_solicit'] = True                        
                
                usuarios.append(user_dict)

            return render(request, 'usuarios.html', {'usuarios':usuarios})
        
        # Alterando no banco.
        elif request.method == "POST":
            data = json.loads(request.POST.get('data'))
            return alter_user(data)
            


## FUNCOES AUXILIARES PARA A FUNCAO USUARIOS ##

# Função para alterar função ou agravos permitidos de um usuário listado.
def alter_user(data):
    
    obj_user = get_user_model().objects.get(id=data['id'])
    
    # Alterar permissão de agravos.
    if data['alterar_agravo']:
        if data['checked']:
            if data['agravo'] in obj_user.lista_agravos_possivel:
                obj_user.lista_agravos_possivel.remove(data['agravo'])
            
            obj_user.lista_agravos_permite.append(data['agravo'])
        
        elif not data['checked']:
            obj_user.lista_agravos_permite.remove(data['agravo'])

        obj_user.save()

    # Alterar função.
    elif data['alterar_funcao']:
        obj_user.funcao = data['funcao']
        obj_user.save()
    
    return JsonResponse({"response":203})


# Funçao para organizar a hierarquia dos usuários.
def hierarchy_has_change():
    hierarquia = {
        'admin':1,
        'gerencia_executiva':2,
        'gerencia_operacional':3,
        'chefia_nucleo':4,
        'area_tecnica':5,
        'gerencia_regional':6,
        'municipal':7,
        'autocadastro':8,
    }
    
    # Gravando a hierarquia em usuarios que ainda nao a tem.
    usuarios = get_user_model().objects.all()
    has_change = False
    if usuarios:
        for user in usuarios:       
            if user.numero_hierarquia != hierarquia[user.funcao]:
                user.numero_hierarquia = hierarquia[user.funcao]
                user.save()
                has_change = True
    
    return has_change


# Função para permitir todos os agravos ao admin caso ainda nao tenha.
def admin_has_change():
    admin_sem_agravos = get_user_model().objects.all().filter(funcao="admin").filter(Q(lista_agravos_permite=None) | Q(lista_agravos_permite=[]))
    has_change = False
    if admin_sem_agravos:
        for user in admin_sem_agravos:        
            user.lista_agravos_permite = AGRAVOS
            user.save()
            has_change = True
    
    return has_change
