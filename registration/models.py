from email.policy import default
from random import choices
from secrets import choice
from tabnanny import verbose
from tokenize import blank_re
from unittest.util import _MAX_LENGTH
from django.db import models
# Paso 1: Importamos de Django el modelo de datos de Usuario:
from django.contrib.auth.models import User
# Paso 2: Importo de la clase constrain el metodo CASCADE:
from django.db.models.deletion import CASCADE
# Paso 3: Importar modulo de cambios receiver
from django.dispatch import receiver
# Paso 4: Importar el metodo para sobreescribirlo
from django.db.models.signals import post_save
# Paso 5: Incluir Types:
from core.types.generos import Generos
from core.types.tipoId import TiposIdentificacion

# Paso 6: Función Global para guardar imagen de perfil de usuario:
def subir_avatar(instance, nombre_archivo):
    anterior_instancia = PerfilUsuario.objects.get(pk = instance.pk)
    anterior_instancia.img_perfil.delete()
    return 'perfiles/' + nombre_archivo

# Paso 7: Create your models here.

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete = CASCADE)
    img_perfil = models.ImageField(upload_to = subir_avatar, null = True, blank = True)
    genero_user = models.CharField(verbose_name = "Género", choices = Generos, max_lenght = 20, null = False, default = "Otro")
    tipo_identificacion = models.CharField(verbose_name = "Tipo de Documento de Identidad", choices = TiposIdentificacion, max_lenght = 50, null = False, default = "Sin Identificar")
    identificacion_usuario = models.CharField(verbose_name = "Número de Identificación", max_lenght = 50, null = False,)
    direccion = models.TextField(verbose_name = "Dirección Postal", null = True, blank = True)
    telefono = models.CharField(verbose_name = "Teléfono", max_length=20, null = True, blank = True)
    # Atributos de Auditoria:
    create_at = models.DateField(auto_now = False, auto_now_add = True, verbose_name = "Fecha de creación", null = True, blank = True) 
    modify_at = models.DateField(auto_now = True, auto_now_add = False, verbose_name = "Fecha de actualización", null = True, blank = True)

    # Metadata del Modelo:
    class Meta:
        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfiles de Usuarios'
        ordering = ['usuario__username']

# Función usa decoradores para usuarios que se encuentren creados:
@receiver(post_save, sender = User)
def ensure_profile_exist(sender, instance, **kwargs):
    if kwargs.get('created', False):
        PerfilUsuario.objects.get_or_create(usuario=instance)
