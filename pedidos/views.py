from django.shortcuts import render, HttpResponse, redirect
# Paso 1. Importar la clase ListView
from django.views.generic import ListView, TemplateView

# Importamos el modelo de datos de productos:
from pedidos.models import Producto, Categoria

# Importar la clase carro a la vista:
from .carro import Carro

# Create your views here.
def catalogo(request):
    template = 'pedidos/catalogo.html'
    # Query a la base de datos:
    productos = Producto.objects.all()

    return render(request, template, {'productos': productos})

class CatalogoView(ListView):
    model = Producto
    paginate_by = 6

# Vistas del carrito de compras:
class carritoCompras(TemplateView):
    template_name = 'pedidos/carrito.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

def agregar_Producto(request, producto_id):
    carro = Carro(request)                              # Creamos un objeto de la clase carro
    producto = Producto.objects.get(id = producto_id)   # Ejecuto el query a la base de datos para que me traiga el producto agregado
    # Ejecutamos el método agregarProducto:
    carro.agregarProducto(producto = producto)          # Pasamos la tupla del query al método de Carro
    return redirect('pedidos:catalogo')                 # Redireccionamos al catalogo de productos




