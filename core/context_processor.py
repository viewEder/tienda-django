# Importamos el modelo de datos de productos:
from pedidos.models import Categoria, SubCategoria

def verInstituto(request):
    my_diccionary = {'instituto': 'Fundación View'}

    return my_diccionary

# Función para traer todas las categorias del modelo de datos:
def catalogoCategoria(request):
    # Query a la base de datos:
    categorias = Categoria.objects.all()
    subcategorias = SubCategoria.objects.all()
    return  {'categorias': categorias, 'subcategorias': subcategorias}

# Diccionario del carrito de compras:
def carritoCompras(request):
    total = 0
    subtotal = 0
    cantidades = 0
    iva_pedido =  0
    # Validación de que el carro exita:
    if 'carro' not in request.session:
        request.session['carro'] = {}
    # Validación si usuario está autenticado:
    if request.user.is_authenticated:
        for key, value in request.session['carro'].items():
            total = total + (float(value['precio']) * (float(value['cantidad'])))
            cantidades = cantidades + (int(value['cantidad']))
            subtotal = round((total / 1.19 ),2)
            iva_pedido = round((total - subtotal),2)
    return { 'Total_Carro': total, 'Cantidad_Carro': cantidades, 'subtotal': subtotal, 'iva_pedido': iva_pedido }
