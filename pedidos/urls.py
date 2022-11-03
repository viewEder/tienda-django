# Importar librerias de rutas
from django.urls import path
# Importar vistas
# from .views import catalogo
from pedidos import views
# Importando vistas basadas en clases:
from .views import CatalogoView, carritoCompras

# Apadrinar rutas:
app_name = 'pedidos'

urlpatterns = [
    path('', views.catalogo, name='listado'),
    path('catalogo/', CatalogoView.as_view(), name = 'catalogo'),
    # Urls del carrito de compras:
    path('carrito/', carritoCompras.as_view(), name = 'carrito'),
    path('agregar/<int:producto_id>', views.agregar_Producto, name='agregar'),
    path('adicionar/<int:producto_id>', views.adicionar_Producto, name='adicionar'),
    path('eliminar/<int:producto_id>', views.eliminar_Producto, name='eliminar'),
    path('restar/<int:producto_id>', views.restar_Producto, name='restar'),
    path('vaciar/', views.vaciar_Carro, name='vaciar'),
]
