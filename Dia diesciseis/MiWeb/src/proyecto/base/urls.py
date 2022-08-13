from django.urls import path
from . import views

urlspatterns = [path('', views.lista_pendientes, name='pendientes')]