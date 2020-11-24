from .admin import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser,Shipper
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from phonenumber_field.formfields import PhoneNumberField


class MerchantRegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('company_name', 'company_reg', 'first_name', 'last_name', 'email', 'address', 'state', 'telephone', 'bio',)


class MerchantEditForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('company_name', 'first_name', 'last_name', 'email', 'address', 'state', 'telephone', 'bio', 'password')


class ShopperRegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'telephone')


class ShopperEditForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'telephone')


class ShipperRegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'address', 'state', 'telephone', 'bio', )


class ShipperEditForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('company_name', 'first_name', 'last_name', 'email', 'address', 'state', 'telephone',)


location_options = [('Lagos', 'Lagos'), ('Abuja', 'Abuja'), ('Port Harcourt', 'Port Harcourt'), ('South-South',
                    'South-South'), ('South-East', 'South-East'), ('South-West', 'South-West'), ('North-East',
                    'North-East'), ('North-Central', 'North-Central'), ('North-West', 'North-West')]
unit_options = {('kilogram', 'Kilogram'), ('Grams', 'Grams')}
transport_type = [('Bike', 'Bike'), ('MiniBus', 'MiniBus')]


class ShipperForm(forms.ModelForm):
    extra_info = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':
                                                                 'Additional Information'}))
    unit = forms.ChoiceField(label='', widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Unit'}),
                             choices=unit_options)
    region = forms.ChoiceField(label='', widget=forms.Select(attrs={'class': 'form-control', 'placeholder':
                                                                    'Region'}), choices=location_options)
    extra_weight = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                                'placeholder': 'Telephone'}))
    engine_number = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':
                                                                                 'Engine Number'}))
    registration_number = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                                       'placeholder': 'Price'}))
    registration_name = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':
                                                                               'Pick Up'}),)
    year_of_purchase = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                                    'placeholder': 'Price'}))
    brand = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Pick Up'}))
    vehicle_type = forms.ChoiceField(label='', widget=forms.Select(attrs={'class': 'form-control', 'placeholder':
                                                                          'Pick Up'}), choices=transport_type)
    license_number = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder'
                                                                                  : 'Price'}))

    class Meta:
        model = Shipper
        fields = ('vehicle_type', 'registration_name', 'registration_number', 'license_number', 'engine_number', 'brand',
                  'year_of_purchase', 'region', )
