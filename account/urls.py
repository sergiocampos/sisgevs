from inspect import signature
from django.urls import path
from numpy import sign
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signup, name='signup'),

]