from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render




# Renderiza a pagina de formulário para criar um novo caso
@login_required(login_url='/login')
def criar_caso(request):
    return render(request, 'act_criar_caso.html')


# Capta o submit do formulario de criar caso.
@login_required(login_url='/login')
def set_criar_caso(request):
    for key, value in request.POST.items():
        print(f"KEY: {key} | VALUE: {value}")
    # TODO: Receber os dados do request, validar e salvar em banco.
    pass


# Renderiza a pagina de edição de caso.
@login_required(login_url='/login')
def editar_caso(request, id):
    # TODO: Renderizar pagina com os dados captados no id.
    pass


# Salva as alterações de caso.
@login_required(login_url='/login')
def set_editar_caso(request):
    # TODO: Receber os dados do request, validar e salvar em banco a edição do caso.
    pass


# Renderiza pagina apenas para visualização de um caso.
@login_required(login_url='/login')
def editar_caso(request, id):
    # TODO: Renderizar pagina com os dados captados no id
    pass
