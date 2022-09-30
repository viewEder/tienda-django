from django.shortcuts import render

# Importar los elementos que creamos:
from .forms import PerfilForm
# Implementar Vistas Bassadas en Clases de Django:
from django.views.generic.edit import UpdateView
# Decoradores del Login:
from django.utils.decorators import method_decorator        # Método decorador para usuario logueado y uso de la vista:
from django.contrib.auth.decorators import login_required   # Método de requiere inicio de sesión:
# Importamos el modelo de datos
from .models import PerfilUsuario
# Cargamos el formulario de creacion de usuarios:
from django.contrib.auth.forms import UserCreationForm      # Formulario por defecto de creación de usuario
from django.urls import reverse_lazy                        # Función para redireccionar a una url
from django import forms                                    # Importamos las propiedades del formulario

# Create your views here.
@method_decorator(login_required, name='dispatch')
class PerfilUpdate(UpdateView):
    form_class = PerfilForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/perfil_form'

    # Sobreescribimos el método get_object:
    def get_object(self):
        perfil, creado = PerfilUsuario.objects.get_or_create(usuario = self.request.user)
        return perfil