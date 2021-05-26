from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('register_shopper/', views.register_shopper, name='register_shopper'),
    path('register_merchant/', views.register_merchant, name='register_merchant'),
    path('register_shipper/', views.register_shipper, name='register_shipper'),
    path('edit_user/', views.edit_user, name='edit_user'),
    path('create_shipper_details/', views.create_shipper_details, name='create_shipper_details'),
    path('edit_shipper_details/', views.edit_shipper_details, name='edit_shipper_details'),
    path('change_password/', views.change_password, name='change_password'),
    path('profile/', views.profile, name='profile'),
    path('setting/', views.account_setting, name='settings'),
    path('profile/<int:pk>/', views.view_profile, name='view_profile'),
]