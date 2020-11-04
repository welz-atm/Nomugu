from .admin import UserCreationForm , UserChangeForm
from django import forms
from .models import CustomUser,Shipper
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from phonenumber_field.formfields import PhoneNumberField


class MerchantRegisterForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    address = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':
                                                                      'Address'}))
    state = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}))
    country = CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget(attrs={'class':
                                                                                                'form-control'}))
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':
                                                                   'Company Name'}))
    telephone = PhoneNumberField()
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                         'placeholder': 'Contact Person First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Contact Person Last Name'}))
    bio = forms.CharField(label='',
                          widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Company Bio'}))

    class Meta:
        model = CustomUser
        fields = ('name', 'first_name', 'last_name', 'email', 'address', 'state', 'country', 'telephone','bio',)

    def __init__(self, *args, **kwargs):
        super(MerchantRegisterForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].label = ''
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''


class MerchantEditForm(UserChangeForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}))
    address = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Address'}))
    state = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'State'}))
    telephone = PhoneNumberField()
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Company Name'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                         'placeholder': 'Contact Person First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':
                                                                        'Contact Person Last Name'}))
    country = CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget(attrs={'class':
                                                                                                'form-control' }))
    bio = forms.CharField(label='',
                          widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Company Bio'}))
    password = forms.CharField(label='',widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = CustomUser
        fields = ('name','first_name','last_name','email','address','state','country','telephone','bio')


class ShopperRegisterForm(UserCreationForm):
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}))
    telephone = PhoneNumberField()
    first_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'placeholder':'First Name'}))
    last_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control',
                                                                       'placeholder':'Last Name'}))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'telephone')

    def __init__(self, *args, **kwargs):
        super(ShopperRegisterForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].label = ''
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''


class ShopperEditForm(UserChangeForm):
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}))
    telephone = PhoneNumberField()
    password = forms.CharField(label='',widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'telephone')


class ShipperRegisterForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                     'placeholder': 'Company Email'}))
    address = forms.CharField(label='',
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Address'}))
    state = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}))
    company_reg = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                   'placeholder': 'Company Registration Number'}))
    country = CountryField(blank_label='(select country)').formfield(
        widget=CountrySelectWidget(attrs={'class': 'form-control'}))
    name = forms.CharField(label='',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}))
    telephone = PhoneNumberField()
    first_name = forms.CharField(label='',
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Contact First Name'}))
    last_name = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':
                                                              'Contact Last Name'}))

    class Meta:
        model = CustomUser
        fields = ('name', 'first_name', 'last_name', 'email', 'company_reg', 'address', 'state', 'country', 'telephone',)

    def __init__(self, *args, **kwargs):
        super(ShipperRegisterForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].label = ''
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''


class ShipperEditForm(UserChangeForm):
    email = forms.EmailField(label='',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Email'}))
    address = forms.CharField(label='',
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Address'}))
    state = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}))
    country = CountryField(blank_label='(select country)').formfield(
        widget=CountrySelectWidget(attrs={'class': 'form-control'}))
    name = forms.CharField(label='',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}))
    telephone = PhoneNumberField()
    first_name = forms.CharField(label='',
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'placeholder': 'Contact First Name'}))
    last_name = forms.CharField(label='',
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Contact Last Name'}))
    password = forms.CharField(label='',widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = CustomUser
        fields = ('name', 'first_name', 'last_name', 'email', 'company_reg', 'address', 'state', 'country', 'telephone',)


location_options = [('Lagos', 'Lagos'), ('Abuja', 'Abuja'), ('Port Harcourt', 'Port Harcourt'), ('South-South',
                    'South-South'), ('South-East', 'South-East'), ('South-West', 'South-West'), ('North-East',
                    'North-East'), ('North-Central', 'North-Central'), ('North-West', 'North-West')]
unit_options = {('kilogram', 'Kilogram'), ('Grams', 'Grams')}
transport_type = [('Bike', 'Bike'), ('MiniBus', 'MiniBus')]


class ShipperForm(forms.ModelForm):
    price = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':
                                                                         'Price'}))
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
                  'year_of_purchase', 'region', 'price', 'unit', 'extra_weight', 'extra_info')
