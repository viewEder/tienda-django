from django.shortcuts import render, HttpResponse
# Paso 1. Importar la clase ListView
from django.views.generic import ListView 

# Importamos el modelo de datos de productos:
from pedidos.models import Producto, Categoria

# Create your views here.
def catalogo(request):
    template = 'pedidos/catalogo.html'
    # Query a la base de datos:
    productos = Producto.objects.all()

    return render(request, template, {'productos': productos})

class CatalogoView(ListView):
    model = Producto
    paginate_by = 6

