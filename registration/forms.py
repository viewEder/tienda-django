# Importar librerias
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import widgets
# Importar el modelo de dato:
from .models import PerfilUsuario

# Formulario para el perfil de usuario:
class PerfilForm(forms.ModelForm):
    # Pasamos la metadata del formulario:
    class Meta:
        model = PerfilUsuario
        fields = ['nombre_completo', 'complemento_dirección', 'img_perfil','genero_user','tipo_identificacion','identificacion_usuario','direccion','telefono']
        widgets = {
            'nombre_completo' : forms.TextInput(attrs = {'class':'form-control mt-2'}),
            'complemento_dirección': forms.Textarea(attrs = {'class':'form-control mt-2', 'rows': '3', 'placeholder': '(Apartamento, Calle, Transversal, atravesando el pasillo... etc).'}),
            'img_perfil' : forms.ClearableFileInput(attrs = {'class':'form-control mt-2'}),
            'genero_user' : forms.Select(attrs = {'class':'form-select mt-2'}),
            'tipo_identificacion' : forms.Select(attrs = {'class':'form-select mt-2'}),
            'identificacion_usuario' : forms.TextInput(attrs = {'class':'form-control mt-2'}),
            'direccion' : forms.Textarea(attrs = {'class':'form-control mt-2', 'rows': '1'}),
            'telefono' : forms.TextInput(attrs = {'class':'form-control mt-2'}),
        }

