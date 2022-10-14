# Importar librerias de rutas
from django.urls import path
# Importar vistas
# from .views import catalogo
from pedidos import views

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
]
