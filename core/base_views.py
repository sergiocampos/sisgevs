from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render



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


# TODO: Função responsável por retornar as notificações referente a pesquisa.


# TODO: Função responsável por exportar dados.


# TODO: Função responsável por cancelar um dado.

