from django import forms
from .models import Product, Category

shipping_type = (('initial', '...Choose Shipping...'), ('free shipping', 'Free Shipping'),('free shipping(lagos only)',
                 'Free Shipping(Lagos Only)'), ('depends on size/location', 'Depends on size/location'))

unit_options = [('Kilogram', 'Kilogram'), ('Gram', 'Gram'), ('Tonnes', 'Tonnes')]

NAMES = (('Air Conditioner', 'Air Conditioner'), ('Android', 'Android'), ('Audio', 'Audio'), ('Blender', 'Blender'),
         ('Bed/Mattress', 'Bed/Mattress'), ('Clothing', 'Clothing'), ('Cooker', 'Cooker'), ('Desktop', 'Desktop'),
         ('Dispenser', 'Dispenser'), ('Fabrics', 'Fabrics'), ('Fans', 'Fans'), ('Footwear', 'Footwear'),
         ('Fragrance', 'Fragrance'), ('Freezer', 'Freezer'), ('Fruit', 'Fruit'), ('Furniture', 'Furniture'),
         ('IOS', 'IOS'), ('Kettle', 'Kettle'), ('Laptop', 'Laptop'), ('Microwave', 'Microwave'),
         ('Networking', 'Networking'), ('Refrigerator', 'Refrigerator'), ('Server', 'Server'),
         ('Television', 'Television'), ('Washers', 'Washers'), ('Watch', 'Watch'))


class ProductForm(forms.ModelForm):
    name = forms.ChoiceField(label='', widget=forms.Select(attrs={'placeholder': 'Unit'}), choices=NAMES)
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    brand = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Brand'}))
    quantity = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'placeholder': 'Quantity'}))
    category = forms.ModelChoiceField(label='', widget=forms.Select(attrs={'placeholder': 'Unit'}),
                                      queryset=Category.objects.all())
    image = forms.ImageField(label='', widget=forms.FileInput(attrs={'placeholder': 'Choose your Image'}))
    unit = forms.ChoiceField(label='', widget=forms.Select(attrs={'placeholder': 'Unit'}), choices=unit_options)
    weight = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'placeholder': 'Weight of product'}))
    price = forms.IntegerField(label='',
                               widget=forms.NumberInput(attrs={'placeholder': 'Price'}))
    description = forms.CharField(label='', max_length=2000, widget=forms.Textarea(attrs={'placeholder':
                                                                                              'Product Description'}))

    class Meta:
        model = Product
        fields = ('name','category','title','brand','quantity','weight','unit','image','price', 'description')