
from django.contrib.auth import (authenticate, login, logout, update_session_auth_hash)
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_protect
from core.base_views import AGRAVOS as agravos
from django.shortcuts import redirect, render
from django.forms import ValidationError
from django.contrib import messages
from core.models import Municipio
from django.conf import settings
from .models import User
import urllib
import json

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
		agravos_solicit = request.POST.get('agravos-select')
		agravos_solicit = agravos_solicit.split(',') if agravos_solicit else []
		
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
				municipio = Municipio.objects.get(id=municipio_id),
				lista_agravos_possivel=agravos_solicit,
				lista_agravos_permite=[],
			)
			storage = messages.get_messages(request)
			storage.used = True
			messages.success(request, 'Conta cadastrada com sucesso!')
			return redirect("login_page")
		
	municipios = Municipio.objects.all()
	return render(request, template_name, {'municipios': municipios, 'agravos':agravos})


def login_page(request):
	storage = messages.get_messages(request)
	storage.used = True
	return render(request, 'login_page.html')


@csrf_protect
def login_submit(request):
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username = username, password = password)

		
		''' Begin reCAPTCHA validation '''
		recaptcha_response = request.POST.get('g-recaptcha-response')
		url = 'https://www.google.com/recaptcha/api/siteverify'
		values = {
				'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
				'response': recaptcha_response
			}
		data = urllib.parse.urlencode(values).encode()
		req =  urllib.request.Request(url, data=data)
		response = urllib.request.urlopen(req)
		result = json.loads(response.read().decode())
		''' End reCAPTCHA validation '''
		if result['success']:
			if user is not None:
				login(request, user)
				#return redirect('/all_forms/')
				return redirect('/')
			else:
				messages.error(request, 'Senha ou usuário inválidos.')
				return render(request, 'login_page.html')

			#form.save()
			messages.success(request, 'New comment added with success!')

		else:
			messages.error(request, 'CAPTCHA inválido. Tente novamente.')
		
			#messages.error(request, 'Usuário e/ou senha inválido!')
	return redirect('/login/')


@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/')


@login_required
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			messages.success(request, ('Your password was successfully updated!'))
			return redirect('/all_forms/')
		else:
			messages.error(request, ('Please correct the error below.'))
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'change_password.html', {'form': form})
	