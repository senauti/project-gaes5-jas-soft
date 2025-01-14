import os

from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.views.generic.list import ListView
from .models import Pays, PurchaseOrder, Sales, Employed
from .utils import breadcrumb
from .utils import get_or_create_order
from .models import Order
from carts.utils import get_or_create_cart
from django.contrib.auth.decorators import login_required

from .models import Sales
from postulation.models import Employed

# Create your views here.

@login_required(login_url='login_jas')
def order(request):
        cart = get_or_create_cart(request)
        order = get_or_create_order(cart, request)
                
        return render(request,'sales/orders/orden.html',{
                'cart': cart,
                'order': order,
                'breadcrum':breadcrumb()
        })
        
@login_required(login_url='login_jas')      
def address(request):
        cart = get_or_create_cart(request)
        order = get_or_create_order(cart, request)
        
        shipping_address =  order.get_or_set_shipping_address() 
        
        return render(request, 'sales/address.html',{
                'cart':cart,
                'order':order,
                'breadcrum':breadcrumb(address=True)
        })
        


class SaleInvoicePdfView(View):
          
    def link_callback(self, uri, rel):
            """
            Convert HTML URIs to absolute system paths so xhtml2pdf can access those
            resources
            """
            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL        # Typically /static/
                    sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                    mUrl = settings.MEDIA_URL         # Typically /media/
                    mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                    if uri.startswith(mUrl):
                            path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                            path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                            return uri

            # make sure that file exists
            if not os.path.isfile(path):
                    raise RuntimeError(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path
        
    def get(self, request, *args, **kwargs):
        
        template = get_template('sales/sale_invoice.html')
        context = {
            'sales': Sales.objects.all(),
            'comp': {'name': 'PROMOPLAST S.A.S', 'addres' : 'BogotÃ¡, Colombia'},
            'icon': '{}{}'.format(settings.STATIC_URL, 'img/logo.png')
            }
        
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="salesreport.pdf"'
        
        html = template.render(context)
        pisa_status = pisa.CreatePDF(   
            html, dest=response,
            #link_callback=self.link_callback
        )
                
        
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response


class SalesListView(ListView):
    template_name = "sales/ventas.html"
    model = Sales
    context_object_name = 'sales'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['message'] = 'VENTAS'
        context['lista_sales'] = Sales.objects.annotate()
        context['pays'] = Pays.objects.all()
        context['purchase_orders'] = PurchaseOrder.objects.annotate()
        context['employed'] = Employed.objects.annotate()  
        return context