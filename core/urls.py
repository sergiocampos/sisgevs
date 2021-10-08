from django.urls import include, path

from . import views

urlpatterns = [
path('', views.CasoEsporotricoseListView.as_view(), name='casoesporotricose_list'),
path('add/', views.CasoEsporotricoseCreateView.as_view(), name='casoesporotricose_add'),
path('<int:pk>/', views.CasoEsporotricoseUpdateView.as_view(), name='casoesporotricose_change'),

]