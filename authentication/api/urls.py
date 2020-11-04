from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

app_name = 'authentication'

urlpatterns = [
    path('register_merchant/', views.register_merchant, name='register_merchant'),
    path('register_shipper/', views.register_shipper, name='register_shipper'),
    path('register_shopper/', views.register_shopper, name='register_shopper'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change+password'),
    path('login/', views.ObtainAuthTokenView.as_view(), name='login'),
]
urlpatterns = format_suffix_patterns(urlpatterns)