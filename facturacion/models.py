from django.db import models
# Importamos el modelo de datos de usuario:
from django.contrib.auth.models import User

# Create your models here.
class FormaPago(models.Model):
    nombre_forma = models.CharField(verbose_name = 'Forma de Pago', max_length = 20)

    class Meta:
        verbose_name_plural = 'Formas de Pago'
    
    def __str__(self):
        return f'{self.nombre_forma}'

class DetallePago(models.Model):
    forma_pago = models.ForeignKey(FormaPago, on_delete = models.CASCADE)
    cliente = models.ForeignKey(User, on_delete = models.CASCADE)
    banco = models.CharField(verbose_name = 'Banco', max_length = 30)
    titular = models.CharField(verbose_name = 'Titular de la cuenta', max_length = 250)
    cc_titular = models.CharField(verbose_name = 'Documento de identidad', max_length = 20)
    total_pago = models.DecimalField(max_digits = 20, decimal_places = 2, verbose_name = "Total a Pagar")
    iva_pago = models.DecimalField(max_digits = 20, decimal_places = 2, verbose_name = "Total a Pagar")
    # Atributos de Auditoria:
    create_at = models.DateField(auto_now = False, auto_now_add = True, verbose_name = "Fecha de creación", null = True, blank = True) 
    modify_at = models.DateField(auto_now = True, auto_now_add = False, verbose_name = "Fecha de actualización", null = True, blank = True)

    class Meta:
        verbose_name_plural = 'Detalle de Pago'
    
    def valorIva(self):
        self.iva_pago = self.total_pago / 1.19
        return self.iva_pago

    def __str__(self):
        return f'{self.cliente} {self.total_pago}'


class Factura(models.Model):
    pass