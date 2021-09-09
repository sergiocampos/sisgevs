from django.shortcuts import render, redirect

# Create your views here.

def login_page(request):
	return render(request, 'login_page.html')


def set_login_page(request):
	return redirect('index')


def index(request):
	return render(request, 'index.html')


def informar_dados_ficha(request):
	return render(request, 'informar_dados_ficha.html')

def localizar_paciente_nome(request):
	return render(request, 'localizar_notificacao_nome.html')