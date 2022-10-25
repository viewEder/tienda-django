from django.contrib import admin
from .models import Categoria, Producto, SubCategoria

# Register your models here.

admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(Producto)
