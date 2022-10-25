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
