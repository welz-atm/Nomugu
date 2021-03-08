from django.db import models
from authentication.models import CustomUser
from django_resized import ResizedImageField


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = ResizedImageField(size=[230, 192], upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.name


unit_options = [('Kilogram', 'Kilogram'), ('Gram', 'Gram'), ('Tonnes', 'Tonnes')]
NAMES = (('Air Conditioner', 'Air Conditioner'), ('Android', 'Android'), ('Audio', 'Audio'), ('Blender', 'Blender'),
         ('Bed/Mattress', 'Bed/Mattress'), ('Clothing', 'Clothing'), ('Cooker', 'Cooker'), ('Desktop', 'Desktop'),
         ('Dispenser', 'Dispenser'), ('Fabrics', 'Fabrics'), ('Fans', 'Fans'), ('Footwear', 'Footwear'),
         ('Fragrance', 'Fragrance'), ('Freezer', 'Freezer'), ('Fruit', 'Fruit'), ('Furniture', 'Furniture'),
         ('IOS', 'IOS'), ('Kettle', 'Kettle'), ('Laptop', 'Laptop'), ('Microwave', 'Microwave'),
         ('Networking', 'Networking'), ('Refrigerator', 'Refrigerator'), ('Server', 'Server'),
         ('Television', 'Television'), ('Washers', 'Washers'), ('Watch', 'Watch'))


class Product(models.Model):
    title = models.CharField(max_length=120)
    name = models.CharField(max_length=120, choices=NAMES)
    brand = models.CharField(max_length=120)
    description = models.TextField(max_length=1000)
    color = models.CharField(max_length=15)
    image_one = ResizedImageField(size=[230, 192], upload_to='media')
    image_two = ResizedImageField(size=[230, 192], upload_to='media', null=True, blank=True)
    image_three = ResizedImageField(size=[230, 192], upload_to='media', null=True, blank=True)
    price = models.IntegerField()
    quantity = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    unit = models.CharField(null=True, blank=True, max_length=12, choices=unit_options)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    merchant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    view_product = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def stock_left(self):
        order = OrderItem.objects.get(product=product, ordered=True)
        total = self.quantity - order.quantity
        return total












