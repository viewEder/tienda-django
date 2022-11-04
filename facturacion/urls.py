# importamos url de django:
from django.urls import path
from .views import GenerarPDF

urlpatterns = [
    path('', GenerarPDF.as_view(), name = 'ejemplopdf'),
]