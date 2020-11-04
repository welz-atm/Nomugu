from django.urls import path
from . import views

urlpatterns = [
    path('create_account/', views.create_account, name='create_account'),
    path('account_details/', views.account_details, name='account_details'),
    path('edit_account/<int:pk>/', views.edit_account, name='edit_account'),
    path('make_payment/<int:pk>/', views.make_payment, name='make_payment'),
    path('payment_page/', views.payment_page, name='payment_page'),
    path('my_payment/', views.my_payment, name='my_payment'),
]
