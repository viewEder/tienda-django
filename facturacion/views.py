from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.views.generic import ListView
from django.views import View
# Modelos:

# Para pdf:
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO

# Create your views here.
class GenerarPDF(View):
    # Usamos método get para modificar lo que queremos ver:
    def get(self, request, *args, **kwargs):
        # pdf a crear:
        template = 'facturacion/pdf/pdf.html'
        dicc_context = {'Usuario': 'Eder Lara Trujillo', 'Mensaje':'Hola Mundo'}
        # Función generar pdf:
        pdf = generarPdf(template, dicc_context)
        # Respuesta:
        response = HttpResponse(pdf,content_type='aplication/pdf')
        response['Content-Disposition'] = 'attachment; filename=ejemplo{}.pdf'.format(
            request.user.first_name,
            request.user.last_name
        )
        return response

def generarPdf(template_name, context = {}):
    template = get_template(template_name)
    html = template.render(context)
    result = BytesIO()
    # El resultado final del pdf:
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    # validamos que el resultado:
    if not pdf.err:
        print(type(result))
        return result.getvalue()
    return None