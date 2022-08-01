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

from core import base_views

from django.conf.urls.static import static, settings


urlpatterns = [
    path('teste', views.teste),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('act/', include('_acidente_transito.urls')),
    path('esp-hum/', include('_esporotricose_humana.urls')),
    
    path('change_password/', views.change_password, name='change_password'),
    path('login/',views.login_page, name='login_page'),
    path('login/submit', views.login_submit),
    path('logout/', views.logout_user, name='logout'),

    path('', base_views.principal, name='redirecionamento'),
    path('dados_user/', base_views.dados_user, name='dados_user'),
    path('all_forms/', base_views.all_forms, name='all_forms'),
    path('usuarios/', base_views.usuarios, name='usuarios'),
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)