from django.shortcuts import render, HttpResponse
# Importamos el modelo de datos de productos:
from pedidos.models import Producto, Categoria

# Create your views here.
def catalogo(request):
    template = 'pedidos/catalogo.html'
    # Query a la base de datos:
    productos = Producto.objects.all()

    return render(request, template, {'productos': productos})