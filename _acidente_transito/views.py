from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from core.models import Gerencia, Municipio, UnidadeSaude
from core.base_views import tem_permissao, my_data as base_notificacoes
from .models import Acidente


# Função de listagem de casos.
@login_required(login_url='/login')
def my_datas(request):    
    return render(request, "act_listagem.html", base_notificacoes(request))


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
    
    # Captando a lista de checkbox.
    dados['responsavel_prestar_apoio_local'] = request.POST.getlist('responsavel_prestar_apoio_local')

    # Captando os dados da gerencia.
    gerencia_id = Municipio.objects.get(nome=dados['municipio_ocorrencia_acidente']).gerencia_id
    dados['gerencia'] = Gerencia.objects.get(id=gerencia_id)
    
    dados['responsavel_pelas_informacoes'] = request.user
        
    del dados['csrfmiddlewaretoken'] # Excluindo o token csrf.

    try:
        Acidente.objects.create(**dados)
    except Exception as e:
        message = messages.error(request, "Algo deu errado, tente novamente.")
        return redirect("/act/my-datas", messages=message)
    else:
        message = messages.success(request, "Acidente cadastrado com sucesso!")
        return redirect("/act/my-datas", messages=message)



# Renderiza a pagina de edição de caso.
@login_required(login_url='/login')
def editar_caso(request, id):

    caso = Acidente.objects.get(id=id)

    if tem_permissao(request, caso):
        municipios = Municipio.objects.all()
        hospitais = UnidadeSaude.objects.all()
        return render(request, 'act_editar_caso.html', {"caso":caso, "municipios":municipios, "hospitais":hospitais})
    else:
        message = messages.error(request, "Vocẽ não tem permissão para editar este caso.")
        return redirect("/act/my-datas", messages=message)


# Salva as alterações de caso.
@login_required(login_url='/login')
def set_editar_caso(request, id):

    caso = Acidente.objects.get(id=id)

    if tem_permissao(request, caso):
        dados = request.POST.dict()
        
        # Captando a lista de checkbox.
        dados['responsavel_prestar_apoio_local'] = request.POST.getlist('responsavel_prestar_apoio_local')
            
        dados['responsavel_edicao'] = request.user.id   # Adicionando o responsável pela edição.    
        del dados['csrfmiddlewaretoken']                # Deletando o token csrf

        try:
            Acidente.objects.filter(id=id).update(**dados)
        except Exception as e:
            message = messages.error(request, "Algo deu errado, tente novamente.")
            return redirect("/act/my-datas", messages=message)
        else:
            message = messages.success(request, "Acidente editado com sucesso!")
            return redirect("/act/my-datas", messages=message)
    else:
        message = messages.error(request, "Vocẽ não tem permissão para editar este caso.")
        return redirect("/act/my-datas", messages=message)

# Renderiza pagina apenas para visualização de um caso.
@login_required(login_url='/login')
def visualizar_caso(request, id):
    
    caso = Acidente.objects.get(id=id)

    if tem_permissao(request, caso):
        municipios = Municipio.objects.all()
        hospitais = UnidadeSaude.objects.all()
        return render(request, 'act_visualizar_caso.html', {"caso":caso, "municipios":municipios, "hospitais":hospitais})
    else:
        message = messages.error(request, "Vocẽ não tem permissão para visualizar este caso.")
        return redirect("/act/my-datas", messages=message)


# Renderiza pagina de casos cancelados
@login_required(login_url='/login')
def casos_cancelados(request):
    casosCancelados = Acidente.objects.all().filter(status_caso="Cancelado")
    return render(request, 'act_casos_cancelados.html', {'regs':casosCancelados})
