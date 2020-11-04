from django.urls import path
from . import views

urlpatterns = [
    path('add_cart/<int:pk>/', views.add_cart,name='add_cart'),
    path('my_cart/', views.my_cart,name='my_cart'),
    path('remove_cart/<int:pk>', views.remove_from_cart,name='remove_cart'),
    path('delivered_orders/', views.delivered_orders, name='delivered_orders'),
    path('picked_up_orders/', views.picked_up_orders, name='picked_up_order'),
    path('available_pickup/', views.available_pickup, name='available_pickup'),
    path('select_order_pickup/', views.select_order_pickup, name='order_pickup'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('generate_invoice/<int:pk>/', views.generate_invoice, name='generate_invoice'),
    path('my_invoice/<int:pk>/', views.invoice_list, name='invoices'),
]