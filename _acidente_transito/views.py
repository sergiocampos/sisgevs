from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render




# Renderiza a pagina de formulário para criar um novo caso
@login_required(login_url='/login')
def criar_caso(request):
    return render(request, 'criar_caso.html')


# Capta o submit do formulario de criar caso.
@login_required(login_url='/login')
def set_criar_caso(request):
    pass
