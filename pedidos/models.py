from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import CASCADE
import os

def subirImagenProducto(instance, filename):
    old_instance = Producto.objects.get(pk=instance.pk)
    # Validamos si existe una imagen anterior
    if old_instance.imagen_producto:
        # asignamos una variable para el manejo del arrchivo:
        imagen = old_instance.imagen_producto
        # Validamos si efectivamente es un archivo:
        if imagen.file:
            # Si es un archivo,tomaremos su ubicación:
            if os.path.isfile(imagen.path):
                # Cerramos el archivo por si se encuentra en uso:
                imagen.file.close()
                # Eliminamos el archivo usando los métodos del sistema operativo:
                os.remove(imagen.path)

    old_instance.imagen_producto.delete()

    return 'productos/' + filename

# Create your models here.
class Categoria(models.Model):
    # Atributos propios
    nombre_categoria = models.CharField(verbose_name = 'Nombre de Categoría', max_length = 50)
    # Atributos de Auditoria:
    create_at = models.DateField(auto_now = False, auto_now_add = True, verbose_name = "Fecha de creación", null = True, blank = True) 
    modify_at = models.DateField(auto_now = True, auto_now_add = False, verbose_name = "Fecha de actualización", null = True, blank = True)

    class Meta:
        verbose_name_plural = 'Categoria'

    def __str__(self):
        return f'{self.nombre_categoria}'

class SubCategoria(models.Model):
    # Atributos propios
    categoria = models.ForeignKey(Categoria, on_delete = CASCADE)
    nombre_subcategoria = models.CharField(verbose_name = 'Nombre de Categoría', max_length = 50)
    # Atributos de Auditoria:
    create_at = models.DateField(auto_now = False, auto_now_add = True, verbose_name = "Fecha de creación", null = True, blank = True) 
    modify_at = models.DateField(auto_now = True, auto_now_add = False, verbose_name = "Fecha de actualización", null = True, blank = True)
    
    class Meta:
        verbose_name_plural = 'Subcategoria'

    def __str__(self):
        return f'{self.nombre_subcategoria}'

class Producto(models.Model):
    subcategoria = models.ForeignKey(SubCategoria, on_delete = CASCADE, null = True, blank = True)
    nombre_producto = models.CharField(verbose_name = "Nombre", max_length = 50)
    descripcion_producto = models.TextField(verbose_name = "Descripcion", null = True, blank = True)
    imagen_producto = models.ImageField(upload_to = subirImagenProducto, verbose_name = "Imagen de Producto", null = True, blank = True)
    costo_producto = models.DecimalField(max_digits = 20, decimal_places = 2, verbose_name = "Costo de Producto")
    valor_venta = models.DecimalField(max_digits = 20, decimal_places = 2, verbose_name = "Valor de Venta de Producto")
    cantidad_stock = models.IntegerField(verbose_name = "Cantidad Disponible", validators=[MinValueValidator(0), MaxValueValidator(9999)])
    disponibilidad = models.BooleanField(default = True)
    # Atributos de Auditoria:
    create_at = models.DateField(auto_now = False, auto_now_add = True, verbose_name = "Fecha de creación", null = True, blank = True) 
    modify_at = models.DateField(auto_now = True, auto_now_add = False, verbose_name = "Fecha de actualización", null = True, blank = True)

    class Meta:
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f'{self.nombre_producto}'
