# Importar librerias de rutas
from django.urls import path
# Importar vistas
# from .views import catalogo
from pedidos import views
# Importando vistas basadas en clases:
from .views import CatalogoView

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('catalogo/', CatalogoView.as_view(), name = 'listado')
]
