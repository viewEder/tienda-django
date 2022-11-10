# importamos url de django:
from django.urls import path
from .views import GenerarPDF, PasarelaPago

urlpatterns = [
    path('facturas/', PasarelaPago.as_view(), name = 'pasarela'),
    path('', GenerarPDF.as_view(), name = 'ejemplopdf'),
]