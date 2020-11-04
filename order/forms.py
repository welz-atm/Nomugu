from django import forms
from .models import OrderItem, Order
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from phonenumber_field.modelfields import PhoneNumberField


QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


class OrderItemForm(forms.ModelForm):
    quantity = forms.TypedChoiceField(label='',choices=QUANTITY_CHOICES,
                                      widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Quantity'}))

    class Meta:
        model = OrderItem
        fields = ('quantity',)


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                         'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Last Name'}))
    telephone = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                             'placeholder': 'Telephone Number'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    address = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Address'}))
    state = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}))
    city = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}))
    country = CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget(attrs={'class':
                                                                                                           'form-control'}))
    telephone = PhoneNumberField()

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'telephone', 'email', 'address', 'state', 'city', )