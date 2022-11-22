from django.shortcuts import render
# importamos paquetes de vistas de clases:
from django.views.generic import TemplateView

# Implementar librerias rest-framework:
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

# Create your views here.
# Controladores con Rest-Framework:
class HomeApiView(APIView):
    """ Test de ApiView """

    # Serializador:
    serializer_class = serializers.HomeSerilizer           # Creando un objeto en la clase HomeSerializer

    # Métodos:
    def get(self, request, format = None):
        """ Lista descriptiva de ApiView """
        apiview_es = [
            'Se usan métodos como funciones (get, post, patch, put, delete',
            'Es similar a una vista tradicional en Django',
            'Nos da mayor control de lógica de la función',
            'Está mapeado manualmente a los URLs',
        ]
        diccionario = {
            'mensaje': 'Hola Mundo desde APIView',
            'data': apiview_es
        }
        # Retornamos lo que queremos ver:
        return Response(diccionario)

    # Metodo post:
    def post(self, request):
        """ Retorna un mensaje con lo que agreguemos en el campo del serializador name """
        serializer = self.serializer_class(data = request.data)
        # Vallidamos si el serializador es válido:
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            mensaje = f'Hola {name}'
            return Response({
                'status': status.HTTP_200_OK,
                'mensaje': mensaje
            })
        # Si no es válido:
        else:
            return Response({
                'status' : status.HTTP_400_BAD_REQUEST,
                'mensaje': serializer.errors
            })
    
    def put(self, request):
        """ Actualiza un objeto (Completo) """
        mensaje = f'Method : PUT'
        return Response({
            'status': status.HTTP_200_OK,
            'mensaje': mensaje
        })

    def patch(self, request):
        """ Actualiza un objeto (Parcialmente) """
        mensaje = f'Method : PATCH'
        return Response({
            'status': status.HTTP_200_OK,
            'mensaje': mensaje
        })

    def delete(self, request):
        """ Elimina un objeto (Completo) """
        mensaje = f'Method : DELETE'
        return Response({
            'status': status.HTTP_200_OK,
            'mensaje': mensaje
        })

class HomePageView(TemplateView):
    # atributos de TemplateView:
    template_name = 'core/index.html'

    # atributos propios:
    dicc_context = {
        'titulo': 'Clases de Django Avanzado',
        'profesor': 'Eder Lara T'
    }

    # Utilizando los métodos de la clase, sobreescribios get:
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.dicc_context)
