from django import forms
from .models import Product,Category

categories = [('Beauty', 'Beauty'), ('Computer/Laptops', 'Computer/Laptops'), ('electronics', 'Electronics'),
              ('Fashion', 'Fashion'), ('Flight', 'Flight'), ('Food', 'Food'), ('Home Appliances', 'Home Appliances'),
              ('Hotel', 'Hotel'), ('Kitchen appliances', 'Kitchen Appliances'), ('Phones/Tablets', 'Phones/Tablets')]

shipping_type = (('initial', '...Choose Shipping...'), ('free shipping', 'Free Shipping'),('free shipping(lagos only)',
                 'Free Shipping(Lagos Only)'), ('depends on size/location', 'Depends on size/location'))

unit_options = [('kilogram', 'Kilogram'), ('Gram', 'Gram')]


class ProductForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
    brand = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brand'}))
    quantity = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Quantity'}))
    category = forms.ChoiceField(label='', widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Unit'}),
                                 choices=categories)
    image = forms.ImageField()
    unit = forms.ChoiceField(label='', widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Unit'}),
                             choices=unit_options)
    weight = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':
                                                                          'Weight of product'}))
    price = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}))
    shipping = forms.ChoiceField(label='', widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Shipping'}),
                                 choices=shipping_type, initial='')
    description = forms.CharField(label='', max_length=2000,widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                         'placeholder':
                                                                                         'Product Description'}))

    class Meta:
        model = Product
        fields = ('name','category','title','brand','quantity','weight','unit','image','price','shipping','description')