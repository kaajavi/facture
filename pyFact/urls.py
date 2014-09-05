from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pyFact.views.home', name='home'),
    url(r'^', include(admin.site.urls)),    
    #url(r'facturacion/^', include('facturacion.urls')),
    url( r'^facturacion/print/(?P<idFactura>[0-9]+)', 'facturacion.views.printFactura', name="printFactura"),
    
)
