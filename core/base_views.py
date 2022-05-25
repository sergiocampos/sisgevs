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


# KEY: AGRAVO URL | VALUE: DADOS DO AGRAVO
AGRAVOS = {
    'esp-hum':CasoEsporotricose.objects.all(),
    'act':Acidente.objects.all(),
}

# Funcoes SES
FUNCOES_SES = ["admin", "gerencia_executiva", "gerencia_operacional","chefia_nucleo", "area_tecnica"]


# Função responsável por retornar a pagina principal.
@login_required(login_url='/login/')
def principal(request):	
	print(request.user.funcao)
	return render(request, 'principal.html')

# Função responsável por retornar a pagina dos dados do usuário.
@login_required(login_url='/login/')
def dados_user(request):
	return render(request, 'dados_user.html')


# TODO: Função responsável por retornar a pagina sub-admin.


# Função responsável por retornar as notificações referente a pesquisa.
@login_required(login_url='/login/')
def my_datas(request):
    
    # Identificando o agravo pela url.
    agravo_url = str(request.path).split('/')[1]

    # Registros da doença escolhida.
    registros = AGRAVOS[agravo_url]

	# Pegando os dados de municipio.
    municipios = Municipio.objects.all()
	
    # Filtrando dados por função do usuário.
    if request.user.funcao == 'admin':

        registros = registros.all().order_by('-data_notificacao').exclude(status_caso='Cancelado')
        
    
    elif request.user.funcao == 'gerencia_executiva':

        registros = registros.all().order_by('-data_notificacao').exclude(status_caso='Cancelado')
        
        
    elif request.user.funcao == 'gerencia_operacional':
    
        user_gerencia_operacional = request.user.gerencia_operacional
        registros = registros.filter(responsavel_gerencia_operacional=user_gerencia_operacional).order_by('-data_notificacao').exclude(status_caso='Cancelado')
        
    
    elif request.user.funcao == 'chefia_nucleo':
    
        user_gerencia_operacional = request.user.gerencia_operacional
        user_nucleo = request.user.nucleo
        registros = registros.filter(
            responsavel_gerencia_operacional=user_gerencia_operacional, 
            responsavel_nucleo=user_nucleo
            ).order_by('-data_notificacao').exclude(status_caso='Cancelado')
        
        
    elif request.user.funcao == 'area_tecnica':    

        user_gerencia_operacional = request.user.gerencia_operacional
        user_nucleo = request.user.nucleo
        user_area_tecnica = request.user.area_tecnica
        registros = registros.filter(
            responsavel_gerencia_operacional=user_gerencia_operacional, 
            responsavel_nucleo=user_nucleo,
            responsavel_area_tecnica=user_area_tecnica
            ).order_by('-data_notificacao').exclude(status_caso='Cancelado')
        
    
    elif request.user.funcao == 'gerencia_regional':
        
        user_gerencia_regional = Municipio.objects.get(id=request.user.municipio_id).gerencia_id
        registros = registros.filter(gerencia_id=user_gerencia_regional).order_by('-data_notificacao').exclude(status_caso='Cancelado')

    
    elif request.user.funcao == 'municipal':
        
        user_municipio_id = request.user.municipio_id
        municipio_user = request.user.municipio
        user_municipio_nome = str(Municipio.objects.filter(id=user_municipio_id)[0])
        user_municipio_nome_upper = str(Municipio.objects.filter(id=user_municipio_id)[0]).upper()
        
        registros = registros.filter(Q(municipio_residencia=user_municipio_id) | Q(municipio_residencia=user_municipio_nome) | Q(municipio_residencia=user_municipio_nome_upper) | Q(responsavel_pelas_informacoes_id=user_municipio_id)).order_by('-data_notificacao').exclude(status_caso='Cancelado')
        
    
    elif request.user.funcao == 'autocadastro':

        autocadastro_id = request.user.id
        municipio_user = request.user.municipio

        registros = registros.filter(responsavel_pelas_informacoes_id=autocadastro_id).order_by('-data_notificacao').exclude(status_caso='Cancelado')
        #registros = CasoEsporotricose.objects.filter(municipio_residencia=municipio_user).order_by('-data_notificacao')

        
    # Criando paginação (DESABILITADO)

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
    casos = AGRAVOS[agravo_url]

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
            casos_filtrados = casos.filter(data_notificacao__range=[filtro_data_inicio,filtro_data_fim]).order_by('-id')

        elif len(filtros_data) == 1 and filtros_data[0] != '':
            filtro_unico_dia = filtros_data[0]
            casos_filtrados = casos.filter(data_notificacao=filtro_unico_dia).order_by('-id')

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
        df = pd.DataFrame(list(casos_response.order_by('-id')))
        for i in df.municipio:
            
            try: # Checando se o valor é diferente de NaN
                i = int(i)
            except:
                continue
            else: # Buscando no modelo municipio o nome de municipio pelo id e alterando o dataframe
                municipio = Municipio.objects.get(id=i)
                df.municipio = df.municipio.replace([i], municipio.nome)

    except:
        return redirect(request.path)

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
    agravo = AGRAVOS[agravo_url]
    
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
            usuarios_sem_hierarquia = get_user_model().objects.all().filter(numero_hierarquia=None)
            if usuarios_sem_hierarquia:
                for user in usuarios_sem_hierarquia:        
                    user.numero_hierarquia = hierarquia[user.funcao]
                    user.save()
            

            user_agravos = request.user.lista_agravos_permite
            user_hierarquia = request.user.numero_hierarquia
                    
            # Separando os usuários com nivel hierarquico menor que o user.
            usuarios_lista = get_user_model().objects.all().filter(numero_hierarquia__gt=user_hierarquia).order_by('id')

            # Filtrando usuários que tem acesso ao agravo que o user gerencia.
            usuarios = []
            for usuario in usuarios_lista:
                user_dict = {
                    'id':usuario.id,
                    'email':usuario.email,
                    'municipio':usuario.municipio,
                    'funcao':usuario.funcao,
                    'telefone':usuario.telefone,
                    'esp_hum':False,
                    'act':False,
                    'act_solicit':False,
                    'esp_hum_solicit':False,
                }

                # Adicionando marcador para o checkbox de agravos permite
                for agravo in usuario.lista_agravos_permite:
                    if agravo in user_agravos:
                        if agravo == 'esp-hum':
                            user_dict['esp_hum'] = True
                        elif agravo == 'act':
                            user_dict['act'] = True
                
                # Adicionando marcador para o checkbox de solicitaçao de agravos
                for agravo_solicit in usuario.lista_agravos_possivel:
                    if agravo_solicit in user_agravos:
                        if agravo_solicit == 'esp-hum':
                            user_dict['esp_hum_solicit'] = True
                        elif agravo_solicit == 'act':
                            user_dict['act_solicit'] = True                        
                
                usuarios.append(user_dict)

            return render(request, 'usuarios.html', {'usuarios':usuarios})
        
        # Alterando no banco.
        elif request.method == "POST":
            data = json.loads(request.POST.get('data'))
            obj_user = get_user_model().objects.get(id=data['id'])

            if data['checked']:
                if data['agravo'] in obj_user.lista_agravos_possivel:
                    obj_user.lista_agravos_possivel.remove(data['agravo'])
                
                obj_user.lista_agravos_permite.append(data['agravo'])
            
            elif not data['checked']:
                obj_user.lista_agravos_permite.remove(data['agravo'])

            obj_user.save()                
            
            return JsonResponse({"response":203})



