"""sisgevs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include
from core import views

from django.conf.urls.static import static, settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('login/',views.login_page, name='login_page'),
    path('login/submit', views.login_submit),
    path('logout/', views.logout_user),
    path('index/', views.index, name='index'),
    path('main/', views.main, name='main'),

    path('change_password/', views.change_password, name='change_password'),

    path('my_datas/', views.my_datas, name='my_datas'),

    path('login/',views.login_page, name='login_page'),
    path('login/submit', views.login_submit),

    path('all_forms/', views.all_forms, name='all_forms'),

    path('caso_esporotricose_create/', views.caso_esporotricose_create, name='caso_esporotricose_create'),
    path('caso_esporotricose_create/submit', views.set_caso_esporotricose_create),
    path('ficha_caso_esporotricose_preencher/', views.ficha_caso_esporotricose_preencher, name='ficha_caso_esporotricose_preencher'),
    path('ficha_caso_esporotricose_preenchido/', views.ficha_caso_esporotricose_preenchido, name='ficha_caso_esporotricose_preenchido'),

    path('ajax_load_unidadesaude', views.ajax_load_unidadesaude, name='ajax_load_unidadesaude'),
    path('ajax_load_ibge', views.ajax_load_ibge, name='ajax_load_ibge'),
    path('ajax_hospitalizacao', views.ajax_hospitalizacao, name='ajax_hospitalizacao'),
    path('ajax_hospitalizacao_ibge', views.ajax_hospitalizacao_ibge, name='ajax_hospitalizacao_ibge'),

    path('ajax_autoctone_uf', views.ajax_autoctone_uf, name='ajax_autoctone_uf'),
    path('ajax_autoctone_municipio', views.ajax_autoctone_municipio, name='ajax_autoctone_municipio'),
    path('ajax_autoctone_distrito', views.ajax_autoctone_distrito, name='ajax_autoctone_distrito'),


    path('login/',views.login_page, name='login_page'),
    path('login/submit', views.set_login_page),
    path('informar_dados_ficha/', views.informar_dados_ficha, name='informar_dados_ficha'),
    path('localizar_paciente_nome/', views.localizar_paciente_nome, name='localizar_paciente_nome'),
    path('localizar_paciente_nome/submit', views.set_localizar_paciente_nome),

    path('caso_view/<id>/', views.caso_view, name='caso_view'),
    path('caso_view_detail/', views.caso_view_detail, name='caso_view_detail'),

    path('download_ficha/', views.download_ficha, name='download_ficha'),
    path('remove_caso_esporotricose/<id>/', views.remove_caso_esporotricose, name='remove_caso_esporotricose'),
    path('index_aberto/', views.index_aberto, name='index_aberto'),
    path('ajax_gal/', views.ajax_gal, name='ajax_gal'),
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)