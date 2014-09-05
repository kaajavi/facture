from django.shortcuts import render
from reportlab.pdfgen import canvas
from django.http import HttpResponse
# Create your views here.
from facturacion.models import Cliente, Factura, Item
    


def printFactura(request, idFactura):    
    fact = Factura.objects.get(id=idFactura) 
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="fc_%s.pdf"' % (str(fact.numero))

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(80, 800, str(fact.cliente.nombre))
    p.drawString(400, 800, str(fact.cliente.cuit))
    p.drawString(80, 750, str(fact.cliente.domicilio))
    a=700    
    for item in fact.items():
        p.drawString(80, a, str(item.observacion))
        p.drawString(500, a, "$ " + str("{0:.2f}".format(item.monto)))
        a = a - 30    
    p.drawString(500, 500, str("{0:.2f}".format(fact.subtotal())))
    p.drawString(500, 480, str("{0:.2f}".format(fact.total()-fact.subtotal())))
    p.drawString(500, 460, str("{0:.2f}".format(fact.total())))

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
