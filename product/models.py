from django.db import models
from authentication.models import CustomUser
from django_resized import ResizedImageField


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = ResizedImageField(size=[230, 192], upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.name


unit_options = [('Kilogram', 'Kilogram'), ('Gram', 'Gram'), ('Tonnes', 'Tonnes')]
NAMES = (('Air Conditioner', 'Air Conditioner'), ('Android', 'Android'), ('Audio', 'Audio'), ('Blender', 'Blender'),
         ('Bed/Mattress', 'Bed/Mattress'), ('Body Cream', 'Body Cream'), ('Clothing', 'Clothing'), ('Cooker', 'Cooker'),
         ('Desktop', 'Desktop'), ('Dispenser', 'Dispenser'), ('Fabrics', 'Fabrics'), ('Fans', 'Fans'), ('Food', 'Food'),
         ('Footwear', 'Footwear'), ('Fragrance', 'Fragrance'), ('Freezer', 'Freezer'), ('Fruit', 'Fruit'),
         ('Furniture', 'Furniture'), ('Fruits', 'Fruits'), ('IOS', 'IOS'), ('Jeans', 'Jeans'), ('Kettle', 'Kettle'),
         ('Laptop', 'Laptop'), ('Lingerie', 'Lingerie'), ('Microwave', 'Microwave'), ('Networking', 'Networking'),
         ('Refrigerator', 'Refrigerator'), ('Server', 'Server'), ('Shirts', 'Shirts'), ('T-Shirts', 'T-Shirts'),
         ('Television', 'Television'), ('Trousers', 'Trousers'), ('Vegetable', 'Vegetable'),
         ('Washing Machine', 'Washing Machine'), ('Watch', 'Watch'), ('Wigs', 'Wigs'))


class Product(models.Model):
    title = models.CharField(max_length=120)
    name = models.CharField(max_length=120, choices=NAMES)
    brand = models.CharField(max_length=120)
    description = models.TextField(max_length=1000)
    color = models.CharField(max_length=15, null=True, blank=True)
    image_one = ResizedImageField(size=[500, 500], upload_to='media')
    image_two = ResizedImageField(size=[500, 500], upload_to='media', null=True, blank=True)
    image_three = ResizedImageField(size=[500, 500], upload_to='media', null=True, blank=True)
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)
    weight = models.IntegerField(null=True, blank=True)
    unit = models.CharField(null=True, blank=True, max_length=12, choices=unit_options)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    merchant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    market = models.ForeignKey('market.Market', on_delete=models.CASCADE)
    view_product = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def stock_left(self):
        if self.quantity == 0:
            return 'Out of Stock'
        else:
            return self.quantity












