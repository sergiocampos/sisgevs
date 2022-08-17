from django.urls import path

from . import views
from core import base_views

app_name = '_acidente_transito'

urlpatterns = [
    path('criar-caso', views.criar_caso, name='criar_caso'),
    path('criar-caso/submit', views.set_criar_caso, name='set_criar_caso'),
    path('my-datas/', views.my_datas, name='my_datas'),
    path("editar-caso/<int:id>", views.editar_caso, name="editar_caso"),
    path('editar-caso/submit/<int:id>', views.set_editar_caso, name="set_editar_caso"),
    path('export-data-xlsx/', base_views.export_data_excel, name='export_data_xlsx'),
    path("visualizar-caso/<int:id>", views.visualizar_caso, name="visualizar_caso"),
    # TODO: visualizar-caso
    # TODO: casos-cancelados
]
