from django.urls import path
from . import views

urlpatterns = [
    path('add_cart/<int:pk>/', views.add_cart, name='add_cart'),
    path('my_cart/', views.my_cart, name='my_cart'),
    path('edit_form/<int:pk>/', views.edit_create_form, name='edit_order'),
    path('remove_cart/<int:pk>/', views.remove_from_cart, name='remove_cart'),
    path('update_cart/<int:pk>/', views.update_cart, name='update_cart'),
    path('delivered_orders/', views.delivered_orders, name='delivered_orders'),
    path('product_delivered/<int:pk>/', views.product_delivered, name='product_delivered'),
    path('picked_up_orders/', views.picked_up_orders, name='picked_up_order'),
    path('view_order/<int:pk>/', views.view_order, name='view_order'),
    path('available_pickup/', views.available_pickup, name='available_pickup'),
    path('select_order_pickup/<int:pk>/', views.select_order_pickup, name='order_pickup'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('generate_invoice/<int:pk>/', views.generate_invoice, name='generate_invoice'),
    path('my_invoice/', views.invoice_list, name='my_invoices'),
    path('attach_picture/<int:pk>/', views.attach_picture, name='attach_picture'),
    path('view_picture/<int:pk>/', views.view_picture, name='view_picture'),
    path('confirm_picture/<int:pk>/', views.confirm_picture, name='confirm_picture'),
    path('disapprove_picture/<int:pk>/', views.disapprove_picture, name='disapprove_picture'),
    path('view_picture/<int:pk>/', views.view_picture, name='view_picture'),
    path('for_delivery/<int:pk>/', views.pick_for_delivery, name='pick_for_delivery'),
    path('invoice_detail/<int:pk>/', views.invoice_detail, name='invoice_detail'),
    path('final_cart/', views.final_cart, name='final_cart'),
]