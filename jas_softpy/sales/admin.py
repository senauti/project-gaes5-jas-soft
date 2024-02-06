from django.contrib import admin

# Register your models here.

from .models import Sales
from .models import Pays
from .models import PurchaseOrder
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html


@admin.register(Sales)
class SalesAdmin(ImportExportModelAdmin):

    change_list_template = "admin/custom_change_list.html"

    list_display = ('SaleDate', 'SaleAmount','SaleSubAmount','SaleIvaAmount','Employed','Pays','PurchaseOrder')
    search_fields = ('Employed',)
    list_editable = ()
    list_filter = ('SaleDate',)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['custom_button'] = format_html('<a class="button" href="{}">Reporte pdf</a>', '/sales/sale_invoice/')
        return super().changelist_view(request, extra_context=extra_context)
    

@admin.register(Pays)
class PaysAdmin(admin.ModelAdmin):
    list_display = ('payAmount', 'payTipe', 'payMethod', 'PurchaseOrder')
    search_fields = ('payAmount',)
    list_editable = ()
    list_filter = ('payAmount',)

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('StockProduct','PurchaseOrderDate','State','Product')
    search_fields = ('State',)
    list_editable = ()
    list_filter = ('State',)

