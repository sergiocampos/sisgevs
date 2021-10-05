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
	return redirect('index')