from django.shortcuts import render

# Importar los elementos que creamos:
from .forms import PerfilForm
# Implementar Vistas Bassadas en Clases de Django:
from django.views.generic.edit import UpdateView
from django.views.generic import CreateView
# Decoradores del Login:
from django.utils.decorators import method_decorator        # Método decorador para usuario logueado y uso de la vista:
from django.contrib.auth.decorators import login_required   # Método de requiere inicio de sesión:
# Importamos el modelo de datos
from .models import PerfilUsuario
# Cargamos el formulario de creacion de usuarios:
from django.contrib.auth.forms import UserCreationForm      # Formulario por defecto de creación de usuario
from django.urls import reverse_lazy                        # Función para redireccionar a una url
from django import forms                                    # Importamos las propiedades del formulario

# Create your views here..
# Clase para registro de usuario
class RegistroView(CreateView):
    # Usar formulario de django para crear usuario:
    form_class = UserCreationForm
    template_name = 'registration/registro.html'

    # Métodos para la vista:
    def get_success_url(self):
        return reverse_lazy('login')

    def get_form(self, form_class = None):
        form = super(RegistroView, self).get_form()
        form.fields['username'].widget = forms.TextInput(attrs = {'class':'form-control mb-1', 'placeholder':'NickName de Usuario'})
        form.fields['password1'].widget = forms.PasswordInput(attrs = {'class':'form-control mb-1', 'placeholder':'Password de Usuario'})
        form.fields['password2'].widget = forms.PasswordInput(attrs = {'class':'form-control mb-1', 'placeholder':'Confirmar Password de Usuario'})

        return form


@method_decorator(login_required, name='dispatch')
class PerfilUpdate(UpdateView):
    form_class = PerfilForm
    success_url = reverse_lazy('perfil')
    template_name = 'registration/perfil_form.html'

    # Sobreescribimos el método get_object:
    def get_object(self):
        perfil, creado = PerfilUsuario.objects.get_or_create(usuario = self.request.user)
        return perfil
