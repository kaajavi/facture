from django.contrib import admin


from django.forms import ModelForm, DateTimeInput
from suit.widgets import SuitDateWidget, SuitTimeWidget, SuitSplitDateTimeWidget, AutosizedTextarea

# Register your models here.

from facturacion.models import Cliente, Factura, Item

class FacturaAdminForm(ModelForm):
    class Meta:
        model = Factura
        widgets = {            
            'fecha': SuitDateWidget,
        }

class ClienteAdminForm(ModelForm):
    class Meta:
        model = Cliente
        widgets = {            
            'observaciones': AutosizedTextarea(attrs={'rows': 3, 'class': 'input-xlarge'}),
        }

class ItemInline(admin.TabularInline):
    model = Item
    extra = 2
    
    

class FacturaAdmin(admin.ModelAdmin):    
    form = FacturaAdminForm
    inlines = [ItemInline]
    list_display = ('numero', 'fecha', 'cliente','iva','subtotalToPesos','totalToPesos','imprimir')
    search_fields = ['numero','cliente']
    list_filter = ('cliente', 'fecha','iva')
    
class ClienteAdmin(admin.ModelAdmin):
    form = ClienteAdminForm
    list_display = ('nombre', 'cuit', 'telefono','email')
    

admin.site.register(Factura, FacturaAdmin)
admin.site.register(Cliente, ClienteAdmin) 