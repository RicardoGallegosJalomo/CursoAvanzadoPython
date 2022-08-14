from django.urls import path
from .views import ListaPendientes

urlspatterns = [path('', ListaPendientes.as_view(), name='pendientes')]