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

# Vistas funcionalidades del carrito de compras:
def agregar_Producto(request, producto_id):
    carro = Carro(request)                              # Creamos un objeto de la clase carro
    producto = Producto.objects.get(id = producto_id)   # Ejecuto el query a la base de datos para que me traiga el producto agregado
    # Ejecutamos el método agregarProducto:
    carro.agregarProducto(producto = producto)          # Pasamos la tupla del query al método de Carro
    return redirect('pedidos:catalogo')                 # Redireccionamos al catalogo de productos

# Vistas funcionalidades del carrito de compras:
def adicionar_Producto(request, producto_id):
    carro = Carro(request)                              # Creamos un objeto de la clase carro
    producto = Producto.objects.get(id = producto_id)   # Ejecuto el query a la base de datos para que me traiga el producto agregado
    # Ejecutamos el método agregarProducto:
    carro.agregarProducto(producto = producto)          # Pasamos la tupla del query al método de Carro
    return redirect('pedidos:carrito')                  # Redireccionamos al catalogo de productos

def eliminar_Producto(request, producto_id):            
    carro = Carro(request)                              # Creamos el objeto carro de la Clase Carro
    producto = Producto.objects.get(id = producto_id)   # Obtenemos el producto y lo tomamos como referencia para sacarlo del carro
    carro.eliminarProducto(producto = producto)         # Eliminamos el producto del carro
    return redirect('pedidos:carrito')                  # Nos redirigimos al carrito de la tienda

def restar_Producto(request, producto_id):
    carro = Carro(request)                              # Creamos el objeto carro de la Clase Carro
    producto = Producto.objects.get(id = producto_id)   # Obtenemos el producto y lo tomamos como referencia para sacarlo del carro
    carro.restarProducto(producto = producto)           # Eliminamos el producto del carro
    return redirect('pedidos:carrito')                  # Nos redirigimos al carrito de la tienda

def vaciar_Carro(request):                              # Funcion Limpiar el carrito completo:
    carro = Carro(request)                              # objeto Carro
    carro.limpiarCarro()                                # Creamos un diccionario vacio
    return redirect('pedidos:catalogo')                 # Actualizamos la sesion.

"""
REquerimiento para pasarelade pago:

Dar opciones de :
1. PSE
2. Tarjeta de Crédito/Debito
    # Nombre de Banco
    # Cédula de titular
    # Nombre Titular
    # Valor

"""
