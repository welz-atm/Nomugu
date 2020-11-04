from django.contrib import admin
from .models import Invoices, OrderItem


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('order', 'owner', 'invoiced_date', 'number')
    list_filter = ('order', 'owner', 'invoiced_date', 'number')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'user',)
    list_filter = ('product', 'quantity', 'user',)


admin.site.register(Invoices, InvoiceAdmin)
admin.site.register(OrderItem, OrderItemAdmin)



