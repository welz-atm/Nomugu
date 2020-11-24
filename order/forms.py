from django import forms
from .models import OrderItem, Order
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from phonenumber_field.modelfields import PhoneNumberField


class OrderItemForm(forms.ModelForm):

    class Meta:
        model = OrderItem
        fields = ('quantity',)


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'telephone', 'email', 'address', 'state', 'city', )