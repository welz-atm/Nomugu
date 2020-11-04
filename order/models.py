from django.db import models
from authentication.models import CustomUser
from product.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


class OrderItem(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True, default=1)
    ordered = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    picked = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, related_name='shopper', on_delete=models.CASCADE)
    shipper = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='dispatch_rider', null=True, blank=True)

    def __int__(self):
        return self.pk

    def get_cost(self):
        return self.quantity * self.product.price


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)
    ordered = models.BooleanField(default=False)
    products = models.ManyToManyField(OrderItem)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=254, null=True, blank=True)
    city = models.CharField(max_length=25, null=True, blank=True)
    state = models.CharField(max_length=15, null=True, blank=True)
    country = CountryField(multiple=False)
    telephone = PhoneNumberField(null=True, unique=True)

    def final_price(self):
        total = 0
        for order in self.products.all():
            total += order.get_cost()
        return total


class Invoices(models.Model):
    owner = models.ForeignKey(Order, on_delete=models.CASCADE)
    order = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(unique=True, validators=[MinValueValidator(10000000),
                                                                  MaxValueValidator(99999999)
                                                                  ])
    invoiced_date = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.number