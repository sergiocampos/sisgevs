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
    path('teste', views.teste),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('', views.index_aberto, name='index_aberto'),
    #path('',views.principal, name='index'),
    #path('login/',views.login_page, name='login_page'),
    path('login/submit', views.login_submit),
    path('logout/', views.logout_user, name='logout'),
    path('index/', views.index, name='index'),
    path('index/ajax_index_aberto', views.ajax_index_aberto, name='ajax_index_aberto'),
    path('index/ajax_filtrar_index_aberto', views.ajax_filtrar_index_aberto, name='ajax_filtrar_index_aberto'),
    path('index/submit', views.ajax_exportar_index_fechado, name='ajax_exportar_index_fechado'),

    path('main/', views.main, name='main'),

    path('change_password/', views.change_password, name='change_password'),

    path('my_datas/', views.my_datas, name='my_datas'),
    path('casos_cancelados', views.casos_cancelados, name='casos_cancelados'),
    path('casos_cancelados/submit', views.export_casos_cancelados, name='export_casos_cancelados'),
    path('login/',views.login_page, name='login_page'),
    path('login/submit', views.login_submit),

    path('all_forms/', views.all_forms, name='all_forms'),

    path('caso_esporotricose_create/', views.caso_esporotricose_create, name='caso_esporotricose_create'),
    path('caso_esporotricose_edit/<int:id>/', views.caso_esporotricose_edit, name='caso_esporotricose_edit'),
    path('caso_esporotricose_edit/<int:id>/submit', views.set_caso_esporotricose_edit),
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

    path('ajax_dados_residencia', views.ajax_dados_residencia, name='ajax_dados_residencia'),
    path('ajax_ibge_municipio_residencia', views.ajax_ibge_municipio_residencia, name='ajax_ibge_municipio_residencia'),
    path('ajax_edicao_uf_cidades', views.ajax_edicao_uf_cidades, name='ajax_edicao_uf_cidades'),


    path('login/',views.login_page, name='login_page'),
    path('login/submit', views.set_login_page),
    path('localizar_paciente_nome/', views.localizar_paciente_nome, name='localizar_paciente_nome'),
    path('localizar_paciente_nome/submit', views.set_localizar_paciente_nome),
    path('search_paciente_nome/', views.search_paciente_nome, name='search_paciente_nome'),
    path('localizar_paciente_data_coleta/', views.localizar_paciente_data_coleta, name='localizar_paciente_data_coleta'),
    path('localizar_paciente_data_coleta/submit', views.set_localizar_paciente_data_coleta),
    path('localizar_paciente_data_coleta/csv', views.csv_localizar_paciente_data_coleta),

    path('caso_view/<id>/', views.caso_view, name='caso_view'),
    path('caso_view_detail/<id>/', views.caso_view_detail, name='caso_view_detail'),

    path('download_ficha/', views.download_ficha, name='download_ficha'),
    path('download_dicionario_dados/', views.download_dicionario_dados, name='download_dicionario_dados'),
    path('remove_caso_esporotricose/<id>/', views.remove_caso_esporotricose, name='remove_caso_esporotricose'),
    path('index_aberto/', views.index_aberto, name='index_aberto'),

    path('ajax_index_aberto', views.ajax_index_aberto, name='ajax_index_aberto'),
    path('ajax_filtrar_index_aberto', views.ajax_filtrar_index_aberto, name='ajax_filtrar_index_aberto'),
    path('submit', views.ajax_exportar_index_aberto, name='ajax_exportar_index_aberto'),
    path('ajax_gal', views.ajax_gal, name='ajax_gal'),

    path('dados_user/', views.dados_user, name='dados_user'),

    path('export_data_csv/', views.export_data_csv, name='export_data_csv'),
    path('export_users/', views.export_users, name='export_users'),
    path('organograma/', views.organograma, name='organograma'),
    path('cancelar_caso_esporotricose', views.cancelar_caso_esporotricose, name='cancelar_caso_esporotricose'),
    path('criar_perfil_municipal/', views.criar_perfil_municipal, name='criar_perfil_municipal'),
    path('checar_login_ajax/', views.checar_login_ajax, name='checar_login_ajax'),

    path('', views.principal, name='principal'),
    path('gerenciar-dados/', views.gerenciar_dados, name="gerenciar-dados")
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)