from django.urls import path
from . import views

urlpatterns = [
    path('register_booking/<int:pk>/', views.register_booking, name='register_booking'),
    path('bookings/', views.all_bookings, name='bookings'),
    path('bookings/<int:pk>/', views.view_booking, name='view_booking'),
    path('booking_picked/<int:pk>/', views.booking_picked, name='booking_picked'),
    path('booking_delivered/<int:pk>/', views.booking_delivered, name='booking_delivered'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('delivered_bookings/', views.all_delivered_booking, name='delivered_bookings'),
    path('picked_bookings/', views.all_picked_booking, name='picked_bookings'),
]