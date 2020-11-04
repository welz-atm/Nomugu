from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    price_offer = forms.IntegerField(label_suffix='', widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                                      'placeholder': 'Price Offer'}))
    destination_address = forms.CharField(label_suffix='', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                         'placeholder': 'Price Offer'}))
    pickup_address = forms.CharField(label_suffix='', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                    'placeholder': 'Price Offer'}))

    class Meta:
        model = Booking
        fields = ('pickup_address', 'destination_address', 'price_offer', )