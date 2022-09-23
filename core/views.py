from django.shortcuts import render
# importamos paquetes de vistas de clases:
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    # atributos de TemplateView:
    template_name: 'core/base.html'

    # atributos propios:
    dicc_context = {
        'titulo': 'Clases de Django Avanzado',
        'profesor': 'Eder Lara T'
    }

    # Utilizando los métodos de la clase, sobreescribios get:
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)