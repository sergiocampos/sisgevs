
#from asyncio.windows_events import NULL

import json
import urllib

import pandas as pd
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import (authenticate, get_user_model, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm

from django.shortcuts import redirect, render

from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_protect


from .models import *

# Create your views here.

def login_page(request):
	storage = messages.get_messages(request)
	storage.used = True
	return render(request, 'login_page.html')


def teste(request):
	return render(request, 'base1.html')
	
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
			messages.success(request, _('Your password was successfully updated!'))
			return redirect('/all_forms/')
		else:
			messages.error(request, _('Please correct the error below.'))
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'change_password.html', {'form': form})


@login_required(login_url='/login/')
def set_login_page(request):
	return redirect('index')

@login_required(login_url='/login/')
def pagina_redirecionamento(request):
	return render(request, 'redirecionamento.html')


