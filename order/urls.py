from django.urls import path
from . import views

urlpatterns = [
    path('add_cart/<int:pk>/', views.add_cart, name='add_cart'),
    path('my_cart/', views.my_cart, name='my_cart'),
    path('remove_cart/<int:pk>/', views.remove_from_cart, name='remove_cart'),
    path('update_cart/<int:pk>/', views.update_cart, name='update_cart'),
    path('delivered_orders/', views.delivered_orders, name='delivered_orders'),
    path('product_delivered/<int:pk>/', views.product_delivered, name='product_delivered'),
    path('picked_up_orders/', views.picked_up_orders, name='picked_up_order'),
    path('view_order/<int:pk>/', views.view_order, name='view_order'),
    path('available_pickup/', views.available_pickup, name='available_pickup'),
    path('select_order_pickup/<int:pk>/', views.select_order_pickup, name='order_pickup'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('my_order/', views.shopper_order, name='shopper_order'),
    path('generate_invoice/<int:pk>/', views.generate_invoice, name='generate_invoice'),
    path('my_invoice/<int:pk>/', views.invoice_list, name='invoices'),
]