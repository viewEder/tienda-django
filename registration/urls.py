# Importar librerias de rutas
from django.urls import path
# Importar vistas
from .views import RegistroView, PerfilUpdate

urlpatterns = [
    path('registro/', RegistroView.as_view(), name='registro'),
    path('profile/', PerfilUpdate.as_view(), name='profile'),
]
