from django.contrib import admin
from .models import Invoices, OrderItem, Order


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('order', 'owner', 'invoiced_date', 'number')
    list_filter = ('order', 'owner', 'invoiced_date', 'number')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'user', 'order_date', 'ordered', 'address', 'state', 'confirm_pickup',
                    'picked_for_delivery')
    list_filter = ('product', 'quantity', 'user',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_date', 'address', 'state', 'user', 'ordered', )


admin.site.register(Invoices, InvoiceAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)



