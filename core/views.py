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
	return render(request, 'localizar_paciente_nome.html')

def set_localizar_paciente_nome(request):
	return render(request, 'resultado_search_caso_nome.html')

def caso_view(request):
	return render(request, 'caso_view.html')

def caso_view_detail(request):
	return render(request, 'caso_view_detail.html')