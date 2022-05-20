from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.db.models import Q

from io import BytesIO
import pandas as pd

from _esporotricose_humana.models import CasoEsporotricose
from _acidente_transito.models import Acidente
from .models import *



# TODO: Função responsável por retornar a pagina principal.
@login_required(login_url='/login/')
def principal(request):	
	print(request.user.funcao)
	return render(request, 'principal.html')

# TODO: Função responsável por retornar a pagina dos dados do usuário.
@login_required(login_url='/login/')
def dados_user(request):
	return render(request, 'dados_user.html')


# TODO: Função responsável por retornar a pagina sub-admin.



#######################################################################
# Função responsável por retornar as notificações referente a pesquisa.
@login_required(login_url='/login/')
def my_datas(request):
    
    # Identificando o agravo pela url.
    agravo_url = str(request.path).split('/')[1]
    
    # Dicionario que pega a url e filtra o models referente.
    agravos = {
        'esp-hum':CasoEsporotricose.objects.all(),
        'act':Acidente.objects.all(),
    }

    # Registros da doença escolhida.
    registros = agravos[agravo_url]

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
    

########################################
# Função responsável por exportar dados.
@login_required(login_url='/login/')
def export_data_excel(request):
    
    # Variaveis de filtro.
    agravo_url = str(request.path).split('/')[1]
    filtro_url = str(request.path).split('/')[2]

    # Nome do arquivo de acordo com a doença.
    file_name = f'notificacoes_{agravo_url}.xlsx'

    # Dicionario que pega a url e filtra o models referente.
    agravos = {
        'esp-hum':CasoEsporotricose.objects.all().values(),
        'act':Acidente.objects.all().values(),
    }
    
    # Pegando todos os casos registrados
    casos = agravos[agravo_url]

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

    # Dicionario que pega a url e filtra o models referente.
    agravos = {
        'esp-hum':CasoEsporotricose.objects.all(),
        'act':Acidente.objects.all(),
    }
    
    # Pegando todos os dados.
    agravo = agravos[agravo_url]
    
    # Filtrando pelo id
    registro = agravo.filter(id=id).values()

    # Se já estiver cancelado, habilita novamente.
    if registro[0]['status_caso'] == 'Cancelado':
        agravo.filter(id=id).update(status_caso=None)
    
    # Caso esteja habilitado, cancela o caso.
    else:		
        agravo.filter(id=id).update(status_caso='Cancelado')

    return redirect(redirect_url)
