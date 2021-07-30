from django.db import models
from authentication.models import CustomUser
from product.models import Product
from django.db.models import Sum
from booking.calc_distance import calc_distance
from django.core.validators import MinValueValidator, MaxValueValidator
from django_countries.fields import CountryField
from django_countries import countries
from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField


class OrderItem(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True, default=1)
    ordered = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    picked = models.BooleanField(default=False)  # order selected by shipper
    confirm_pickup = models.BooleanField(default=False)  # authorize shipper to pick up
    #    picked_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=254, null=True, blank=True)
    country = models.CharField(max_length=60, null=True, blank=True, choices=countries)
    city = models.CharField(max_length=25, null=True, blank=True)
    state = models.CharField(max_length=15, null=True, blank=True)
    user = models.ForeignKey(CustomUser, related_name='shopper', on_delete=models.CASCADE)
    shipper = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orderItems', null=True,
                                blank=True)
    image = models.ForeignKey('Photo', on_delete=models.CASCADE, related_name='photos', null=True, blank=True)
    has_images = models.BooleanField(default=False)
    picked_for_delivery = models.BooleanField(default=False)  # order picked by shipper for delivery

    def __int__(self):
        return self.pk

    def get_cost(self):
        return self.quantity * self.product.price

    def get_weight(self):
        return self.product.weight * self.quantity

    def get_customer_address(self):
        return '{}, {} {}, {}'.format(self.address, self.city, self.state, self.country)

    def stock_left(self):
        return self.product.quantity - self.quantity

    def get_shipper(self):
        if self.shipper is None:
            return 'Not Picked yet'
        return self.shipper.first_name

    def get_status(self):
        if self.confirm_pickup is True:
            return 'Confirmed'
        else:
            return 'Awaiting Confirmation'

    def get_pickup_status(self):
        if self.picked is True:
            return 'Selected'
        else:
            return 'Awaiting Selection by   Shipper'

    def delivery_status(self):
        if self.delivered is True:
            return 'Delivered'

    def shipping_cost(self):
        total = 0
        if self.product.market == 'Online Mall':
            address = '{}, {}, {}'.format(self.product.merchant.address, self.product.merchant.city,
                                          self.product.merchant.state)
            customer_address = '{}, {}, {}'.format(self.address, self.city, self.state)
            distance = calc_distance(address, customer_address)
            cost = distance * 45
            total += cost
        else:
            address = self.product.market.address
            customer_address = '{}, {}, {}'.format(self.address, self.city, self.state)
            distance = calc_distance(address, customer_address)
            cost = distance * 45
            total += cost

        return round(total, 2)


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)
    ordered = models.BooleanField(default=False)
    products = models.ManyToManyField(OrderItem)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    address = models.CharField(max_length=254, null=True, blank=True)
    city = models.CharField(max_length=25, null=True, blank=True)
    state = models.CharField(max_length=15, null=True, blank=True)
    country = CountryField(multiple=False)
    telephone = PhoneNumberField(null=True, unique=True)
    detail_created = models.BooleanField(default=False)

    def product_count(self):
        total = self.products.count()
        return total

    def total_weight(self):
        weight = 0
        for order in self.products.all():
            weight += order.get_weight()
        return weight

    def final_price(self):
        total = 0
        for order in self.products.all():
            standard_weight = 15
            weight = self.products.all().aggregate(Sum("product__weight"))['product__weight__sum']
            if weight >= standard_weight:
                total += order.get_cost()
            else:
                total += order.get_cost()
        return total

    def pickup_price(self):
        total = 0
        for order in self.products.all():
            total += order.shipping_cost()
        return total

    def shipping_cost(self):
        shipping_cost = 1500
        standard_weight = 15
        # next_standard_weight = 35
        weight = self.products.all().aggregate(Sum("product__weight"))['product__weight__sum']
        if weight is None:
            return 0
        elif weight >= standard_weight:
            shipping_cost += 1500
        # elif weight >= next_standard_weight:
        #    shipping_cost += 2000
        return shipping_cost

    def total_price(self):
        return self.final_price() + self.shipping_cost()

    def get_status(self):
        if self.delivered is True:
            return 'Delivered'
        else:
            return 'Pending'


class Invoices(models.Model):
    owner = models.ForeignKey(Order, on_delete=models.CASCADE)
    order = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(unique=True, validators=[MinValueValidator(10000000),
                                                                  MaxValueValidator(99999999)
                                                                  ])
    invoiced_date = models.DateTimeField(auto_now_add=True)
    #    last_saved_date = models.DateTimeField(auto_now_add=True)
    is_created = models.BooleanField(default=False)

    def __int__(self):
        return self.number


class Photo(models.Model):
    main_image = ResizedImageField(size=[1400, 1400], upload_to='media', null=True, blank=True)
    rear_image = ResizedImageField(size=[1400, 1400], upload_to='media', null=True, blank=True)
    front_image = ResizedImageField(size=[1400, 1400], upload_to='media', null=True, blank=True)
    side_image = ResizedImageField(size=[1400, 1400], upload_to='media', null=True, blank=True)
    bottom_image = ResizedImageField(size=[1400, 1400], upload_to='media', null=True, blank=True)
