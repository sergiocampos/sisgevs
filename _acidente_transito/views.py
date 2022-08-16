from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from core.base_views import my_data
from core.models import Gerencia, Municipio, UnidadeSaude
from .models import Acidente



@login_required(login_url='/login')
def my_datas(request):
    data = my_data(request)
    for dado in data['regs'].values():
        print(dado)
    acidentes = Acidente.objects.all()
    return render(request, "act_listagem.html", {"acidentes":acidentes})


# Renderiza a pagina de formulário para criar um novo caso
@login_required(login_url='/login')
def criar_caso(request):
    municipios = Municipio.objects.all().order_by("nome")
    hospitais = UnidadeSaude.objects.all().order_by("nome")
    return render(request, 'act_criar_caso.html', {"hospitais":hospitais, "municipios":municipios})


# Capta o submit do formulario de criar caso.
@login_required(login_url='/login')
def set_criar_caso(request):
    
    dados = request.POST.dict()
    
    responsavel_prestar_apoio_local = request.POST.getlist('responsavel_prestar_apoio_local')
    dados['responsavel_prestar_apoio_local'] = responsavel_prestar_apoio_local
    dados['responsavel_pelas_informacoes'] = request.user
    gerencia_id = Municipio.objects.get(nome=dados['municipio_ocorrencia_acidente']).gerencia_id
    dados['gerencia'] = Gerencia.objects.get(id=gerencia_id)

    del dados['csrfmiddlewaretoken']

    try:
        Acidente.objects.create(**dados)
    except Exception as e:

        # TODO: Retornar uma mensagem de erro.

        raise e
    else:
        
        # TODO: Retornar uma mensagem de sucesso.

        return redirect("/")



# Renderiza a pagina de edição de caso.
@login_required(login_url='/login')
def editar_caso(request, id): 
    caso = Acidente.objects.get(id=id)
    municipios = Municipio.objects.all()
    hospitais = UnidadeSaude.objects.all()
    return render(request, 'act_editar_caso.html', {"caso":caso, "municipios":municipios, "hospitais":hospitais})


# Salva as alterações de caso.
@login_required(login_url='/login')
def set_editar_caso(request, id):

    dados = request.POST.dict()
    
    responsavel_prestar_apoio_local = request.POST.getlist('responsavel_prestar_apoio_local')
    dados['responsavel_prestar_apoio_local'] = responsavel_prestar_apoio_local
    dados['responsavel_edicao'] = request.user.id

    del dados['csrfmiddlewaretoken']

    try:
        Acidente.objects.filter(id=id).update(**dados)

    except Exception as e:

        # TODO: Retornar uma mensagem de erro.

        raise e
    else:
        
        # TODO: Retornar uma mensagem de sucesso.

        return redirect("/")


# Renderiza pagina apenas para visualização de um caso.
@login_required(login_url='/login')
def visualizar_caso(request, id):
    # TODO: Renderizar pagina com os dados captados no id
    pass
