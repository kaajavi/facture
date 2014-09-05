from django.conf.urls import patterns, include, url 
urlpatterns = patterns('', 
                    url( r'^facturacion/factura/print/(?P<idFactura>[0-9]+)', 'facturacion.views.printFactura', name="printFactura"),
                       ) 