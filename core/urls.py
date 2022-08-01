from django.urls import include, path

from . import views

urlpatterns = [
path('', views.CasoEsporotricoseListView.as_view(), name='casoesporotricose_list'),
path('add/', views.CasoEsporotricoseCreateView.as_view(), name='casoesporotricose_add'),
path('<int:pk>/', views.CasoEsporotricoseUpdateView.as_view(), name='casoesporotricose_change'),


path('', base_views.principal, name='principal'),
path('dados_user/', base_views.dados_user, name='dados_user'),

]