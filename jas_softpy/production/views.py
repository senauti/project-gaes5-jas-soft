from typing import Any
from django.views.generic.list import ListView
from django.db.models.functions import TruncDate,TruncMonth
from django.template.loader import get_template


import os

from django.db.models import Sum
from django.views import View
from django.http import HttpResponse
from django.conf import settings
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from .models import Supplies,ProductionOrder


class ProductionInvoicePdfView(View):
    
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
                
                template = get_template('production/product_invoice.html')
                context = {
                'supplies': Supplies.objects.all(),
                'comp': {'name': 'PROMOPLAST S.A.S', 'addres' : 'Bogotá, Colombia'},
                'icon': '{}{}'.format(settings.STATIC_URL, 'img/logo.png')
                }
                
                response = HttpResponse(content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="suppliesreport.pdf"'
                
                html = template.render(context)
                pisa_status = pisa.CreatePDF(   
                html, dest=response,
                #link_callback=self.link_callback
                )
                                        
                if pisa_status.err:
                        return HttpResponse('We had some errors <pre>' + html + '</pre>')
                return response         

class ProductionListView(ListView):
        template_name = "production/ordenpedido.html"
        model = ProductionOrder
        context_object_name = 'production_orders'

        def get_queryset(self):
                return ProductionOrder.objects.annotate(max_date=Max('supplieproduction__Production_OrderDate')).order_by('-max_date')

        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context['message'] = 'PRODUCCION | ORDEN DE PEDIDO'

                daily_production = ProductionOrder.objects.annotate(date=TruncDate('supplieproduction__Production_OrderDate')).values('date').annotate(total_quantity=Sum('quantity_used'))

                daily_labels = [entry['date'].strftime('%Y-%m-%d') for entry in daily_production]
                daily_data = [entry['total_quantity'] for entry in daily_production]

                monthly_production = ProductionOrder.objects.annotate(month=TruncMonth('supplieproduction__Production_OrderDate')).values('month').annotate(total_quantity=Sum('quantity_used'))

                monthly_labels = [entry['month'].strftime('%Y-%m') for entry in monthly_production]
                monthly_data = [entry['total_quantity'] for entry in monthly_production]

                context['daily_chart_labels'] = daily_labels
                context['daily_chart_data'] = daily_data
                context['monthly_chart_labels'] = monthly_labels
                context['monthly_chart_data'] = monthly_data

                production_orders = context['production_orders']
                supplies_info = []

                for production_order in production_orders:
                        supplies_info.append({
                                'order_id': production_order.id,
                                'supplies': production_order.supplies.all(), 
                        })

                context['supplies_info'] = supplies_info

                return context
                       
class SuppliesListView(ListView):
        
        template_name = "supplies/insumo.html"
        queryset = Supplies.objects.all().order_by('supplieCode')
        
        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context['message'] = 'PRODUCCION | INSUMOS'
                print(context)
                return context
        
        
"""      
def editar_orden_pedido(request, pk):
    orden_pedido = get_object_or_404(ProductionOrder, pk=pk)

    if request.method == 'POST':
        form = TuFormulario(request.POST, instance=orden_pedido)
        if form.is_valid():
            form.save()
            # Puedes redirigir a alguna página de éxito o mostrar un mensaje aquí
    else:
        form = TuFormulario(instance=orden_pedido)

    return render(request, 'production/ordenpedido.html', {'form': form})

def eliminar_orden_pedido(request, pk):
    orden_pedido = get_object_or_404(ProductionOrder, pk=pk)

    if request.method == 'POST':
        orden_pedido.delete()
        # Puedes redirigir a alguna página de éxito o mostrar un mensaje aquí
        return redirect('tu_nombre_de_url')  # Cambia 'tu_nombre_de_url' por la URL a la que deseas redirigir

    return render(request, 'ordenpedido.html', {'orden_pedido': orden_pedido})
"""
    