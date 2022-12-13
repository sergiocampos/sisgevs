from django.urls import path
      
from core import base_views
      
from . import views
      
app_name = '_acidentes_transito'
      
urlpatterns = [
      
  path('criar-caso', views.criar_caso, name='criar_caso'),
      
  path('criar-caso/submit', views.set_criar_caso, name='set_criar_caso'),
      
  path('my-datas/', views.my_datas, name='my_datas'),
      
  path("editar-caso/<int:id>", views.editar_caso, name="editar_caso"),
      
  path('editar-caso/submit/<int:id>', views.set_editar_caso, name="set_editar_caso"),
      
  path('export-data-xlsx/', base_views.export_data_excel, name='export_data_xlsx'),
      
  path("visualizar-caso/<int:id>", views.visualizar_caso, name="visualizar_caso"),
      
  path('casos_cancelados/', views.casos_cancelados, name='casos_cancelados'),
      
  path('casos-cancelados/<int:id>', base_views.cancelar_caso, name='cancelar_validar_caso'),
      
  path('export_casos_cancelados/', base_views.export_data_excel, name="export_casos_cancelados"),      

  path('download_ficha/', views.download_ficha, name="download_ficha")
      
]
    