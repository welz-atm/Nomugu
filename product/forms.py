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

    class Meta:
        model = Product
        fields = ('name', 'category', 'market', 'title', 'brand', 'quantity', 'weight', 'unit', 'image_one', 'image_two',
                  'image_three', 'price', 'description', )