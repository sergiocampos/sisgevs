
import os
from django.contrib.auth.decorators import login_required
    
from django.shortcuts import HttpResponse, render, redirect
    
from django.contrib import messages
    
from core.models import Gerencia, Municipio, UnidadeSaude, HospitaisUpas
    
from core.base_views import tem_permissao, my_data as base_notificacoes
from sisgevs import settings
    
from .models import AcidentesTransito

import unidecode

    
# Função de listagem de casos.
@login_required(login_url='/login/')
def my_datas(request):
    
  return render(request, 'aci_listagem.html', base_notificacoes(request))

    
# Renderiza a pagina de formulário para criar um novo caso
@login_required(login_url='/login/')
def criar_caso(request):
  municipios = Municipio.objects.all()    
  #hospitais = UnidadeSaude.objects.all().filter(municipio_id=request.user.municipio.id).order_by('nome')
  hospitais = HospitaisUpas.objects.all().order_by('nome')
  return render(request, 'aci_criar_caso.html', {'municipios':municipios, 'hospitais':hospitais})

    
# Capta o submit do formulario de criar caso.
@login_required(login_url='/login/')
def set_criar_caso(request):
    
  dados = request.POST.dict()    
  # Captando os dados da gerencia.
    
  # gerencia_id = Municipio.objects.get(nome=dados['# FILTRAR DADOS DE MUNICIPIO #']).gerencia_id
    
  # dados['gerencia'] = Gerencia.objects.get(id=gerencia_id)    
  dados['quem_foi_responsavel_por_prestar_apoio_local'] = dados['quem_foi_responsavel_por_prestar_apoio_local'].split(',')
  dados['tipos_veiculos_envolvidos_acidente'] = dados['tipos_veiculos_envolvidos_acidente'].split(',')
  dados['responsavel_pelas_informacoes'] = request.user     
  dados['qual_hospital'] = request.POST['qual_hospital']

  #tratando endereço(removendo acentos) antes do storage.
  dados['bairro_local_acidente'] = unidecode.unidecode(dados['bairro_local_acidente'])
  dados['endereco_local_acidente'] = unidecode.unidecode(dados['endereco_local_acidente'])
    
  del dados['csrfmiddlewaretoken'] # Excluindo o token csrf.
    
  try:
    
    AcidentesTransito.objects.create(**dados)
    
  except Exception as e:
    
    message = messages.error(request, "Algo deu errado, tente novamente.")
    
    return redirect("/aci/my-datas", messages=message)
    
  else:
    
    message = messages.success(request, "Caso cadastrado com sucesso!")
    
    return redirect("/aci/my-datas", messages=message)
    
    
# Renderiza a pagina de formulário para editar um novo caso
@login_required(login_url='/login/')
def editar_caso(request, id):
    
  caso = AcidentesTransito.objects.get(id=id)
    
  if tem_permissao(request, caso):
    
    municipios = Municipio.objects.all()
    
    #hospitais = UnidadeSaude.objects.all()
    hospitais = HospitaisUpas.objects.all().order_by('nome')
    
    return render(request, 'aci_editar_caso.html', {'caso':caso, 'municipios':municipios, 'hospitais':hospitais})
    
  else:
    
    message = messages.error(request, "Vocẽ não tem permissão para editar este caso.")
    
    return redirect("/aci/my-datas", messages=message)   

    
# Capta o submit do formulario de editar caso.
@login_required(login_url='/login/')
def set_editar_caso(request, id):
    
  caso = AcidentesTransito.objects.get(id=id)
    
  if tem_permissao(request, caso):
    
    dados = request.POST.dict()    
    
    # Captando os dados da gerencia.    
    # gerencia_id = Municipio.objects.get(nome=dados['# FILTRAR DADOS DE MUNICIPIO #']).gerencia_id    
    # dados['gerencia'] = Gerencia.objects.get(id=gerencia_id)    

    dados['quem_foi_responsavel_por_prestar_apoio_local'] = dados['quem_foi_responsavel_por_prestar_apoio_local'].split(',')
    dados['tipos_veiculos_envolvidos_acidente'] = dados['tipos_veiculos_envolvidos_acidente'].split(',')
    dados['responsavel_pelas_informacoes'] = request.user
    dados['qual_hospital'] = request.POST['qual_hospital']

    #tratando endereço(removendo acentos) antes do storage.
    dados['bairro_local_acidente'] = unidecode.unidecode(dados['bairro_local_acidente'])
    dados['endereco_local_acidente'] = unidecode.unidecode(dados['endereco_local_acidente'])

        
    del dados['csrfmiddlewaretoken'] # Excluindo o token csrf.

    try:
    
      AcidentesTransito.objects.filter(id=id).update(**dados)
    
    except Exception as e:
    
      message = messages.error(request, "Algo deu errado, tente novamente.")
    
      return redirect("/aci/my-datas", messages=message)
    
    else:
    
      message = messages.success(request, "Caso editado com sucesso!")
    
      return redirect("/aci/my-datas", messages=message)
    
  else:
    
    message = messages.error(request, "Vocẽ não tem permissão para editar este caso.")
    
    return redirect("/aci/my-datas", messages=message)

    
# Renderiza a pagina de formulário para visualizar um caso
@login_required(login_url='/login/')
def visualizar_caso(request, id):
    
  caso = AcidentesTransito.objects.get(id=id)
    
  if tem_permissao(request, caso):
    
    municipios = Municipio.objects.all()
    
    hospitais = UnidadeSaude.objects.all()
    
    return render(request, 'aci_visualizar_caso.html', {'caso':caso, 'municipios':municipios, 'hospitais':hospitais})
    
  else:
    
    message = messages.error(request, "Vocẽ não tem permissão para visualizar este caso.")
    
    return redirect("/aci/my-datas", messages=message)

    
# Renderiza uma lista de casos cancelados
@login_required(login_url='/login')
def casos_cancelados(request):
  if request.user.funcao in ["admin", "gerencia_executiva", "gerencia_operacional","chefia_nucleo", "area_tecnica"]:
    casosCancelados = AcidentesTransito.objects.all().filter(status_caso="Cancelado")
    return render(request, 'aci_casos_cancelados.html', {'regs':casosCancelados})

  else:
    return redirect("/")
  


@login_required(login_url='/login')
def download_ficha(request):
  file_path = os.path.join(settings.MEDIA_ROOT, 'ficha-acidente-transito.pdf')
  if os.path.exists(file_path):
    with open(file_path, 'rb') as fh:
      response = HttpResponse(fh.read(), content_type="application/pdf")
      response['Content-Disposition'] = 'inline; filename' + os.path.basename(file_path)
      return response