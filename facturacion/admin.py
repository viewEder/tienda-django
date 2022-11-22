from django.contrib import admin
from .models import FormaPago, DetallePago

class DetallePagoAdmin(admin.ModelAdmin):
    readonly_fields = ['forma_pago', 'cliente', 'banco', 'titular', 'cc_titular', 'total_pago', 'iva_pago','create_at', 'modify_at']
    list_display = ['forma_pago', 'cliente', 'banco','total_pago', 'iva_pago']
    ordering = ['id', 'create_at', 'modify_at']
    list_filter = ['forma_pago', 'cliente', 'banco']

# Register your models here.
admin.site.register(FormaPago)
admin.site.register(DetallePago, DetallePagoAdmin)