from django.urls import path

from . import views

app_name = '_acidente_transito'

urlpatterns = [
    path('criar-caso', views.criar_caso, name='criar_caso'),
    path('criar-caso/submit', views.set_criar_caso, name='set_criar_caso'),
]
