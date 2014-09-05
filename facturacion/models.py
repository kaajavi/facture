# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.
# Representa el modelo de una entrada en el blog
class Factura(models.Model):    
    numero = models.CharField('Número', max_length=150)
    fecha = models.DateField()    
    cliente = models.ForeignKey("Cliente")
    
    IVA_CHOICES = (
    ('210', '21 %'),
    ('105', '10,5 %'),    
    )
    iva = models.CharField(max_length=100, choices=IVA_CHOICES,
                                      default='210')    
    
    def fecha_de_Factura(self):
        return str(self.fecha)
    
    def __unicode__(self):
        return str(self.numero) + "  - " + str(self.cliente)
    
    def subtotal(self):   
        ret=0.0
        items = Item.objects.filter(factura=self)
        for item in items:
            ret = ret + item.monto 
        return round(ret,2)
    
    def subtotalToPesos(self):
        return "$ " + str("{0:.2f}".format(self.subtotal()))
    
    def total(self):
        return round(self.subtotal() + (self.subtotal()*int(self.iva)/1000),2)
    
    def totalToPesos(self):
        return "$ " + str("{0:.2f}".format(self.total()))
    
    
    
    
    def items(self):
        return Item.objects.filter(factura=self)
    
    def imprimir(self):
        return "<a href='../print/%s'><img src='http://icons.iconarchive.com/icons/treetog/junior/24/printer-icon.png' alt='imprimir'/></a>" % (str(self.id))
    #Aclaraciones
    imprimir.short_description = 'Imprimir'        
    imprimir.allow_tags = True
    
    totalToPesos.short_description = 'Total'
    subtotalToPesos.short_description = 'Subtotal'
        

    #Clientes
class Cliente(models.Model):
    nombre = models.CharField('Razon Social', max_length=200)
    cuit = models.CharField('C.U.I.T.', max_length=13)
    domicilio = models.CharField('Domicilio', max_length=200, blank=True)
    telefono = models.CharField('Telefono', max_length=20, blank=True)
    celular = models.CharField('Celular', max_length=20, blank=True)
    email = models.EmailField('Email', max_length=100, blank=True)
    observaciones = models.CharField('Observaciones', max_length=300, blank=True)
    
    
    def __unicode__(self):
        return ' ' + self.nombre
    
class Item(models.Model):
    factura = models.ForeignKey("Factura")
    observacion = models.CharField('Item', max_length=200)
    monto = models.IntegerField('Monto', max_length=200)