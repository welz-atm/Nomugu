from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('register_user/', views.register_user, name='register_user'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('register_merchant/', views.register_merchant, name='register_merchant'),
    path('register_shipper/', views.register_shipper, name='register_shipper'),
    path('create_shipper_details/', views.create_shipper_details, name='create_shipper_details'),
    path('change_password/', views.change_password, name='change_password'),
    path('profile/', views.profile, name='profile'),
]