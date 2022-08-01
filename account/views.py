from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.password_validation import validate_password
from core.models import Municipio
from django.contrib import messages
from .models import User
from django.contrib.auth.hashers import make_password

# Create your views here.

def signup(request, template_name='signup.html'):
	if request.method == 'POST':
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		login = request.POST.get('login')
		cpf = request.POST.get('cpf').replace('.', '').replace('-', '')
		telefone = request.POST.get('telefone').replace('(', '').replace(')', '').replace('-', '')
		municipio_id = int(request.POST.get('municipio'))
		
		# Solicitaçao de agravos.
		agravo_act = request.POST.get('act')
		agravo_esp = request.POST.get('esp-hum')
		lista_agravos_possivel = []
		if agravo_act:
			lista_agravos_possivel.append(agravo_act)
		if agravo_esp:
			lista_agravos_possivel.append(agravo_esp)

		try:
			if User.objects.filter(login=login).exists():
				raise Exception('Este Login já está sendo utilizado')
			elif User.objects.filter(cpf=cpf).exists():
				raise Exception('Este cpf já está sendo utilizado')
			elif not password1 == password2:
				raise Exception('As senhas digitadas não são iguais')
			validate_password(password1)
		except ValidationError as e:
			for i in e:
				print(i)
				messages.error(request, i)
		except Exception as e:
			messages.error(request, e)
		else:	
			password1 = make_password(password1)
			User.objects.create(
				login = request.POST.get('login'),
				username = request.POST.get('nome'),
				password = password1,
				cpf = cpf,
				telefone = telefone,
				#gerencia_operacional = request.POST.get('gerenciaOp'),
				#nucleo = request.POST.get('nucleo'),
				municipio = Municipio.objects.get(id=municipio_id),
				lista_agravos_possivel=lista_agravos_possivel,
				lista_agravos_permite=[],
			)
			storage = messages.get_messages(request)
			storage.used = True
			messages.success(request, 'Conta cadastrada com sucesso!')
			return redirect("login_page")
			
	municipios = Municipio.objects.all()
	return render(request, template_name, {'municipios': municipios})