from django.db import models
from order.models import OrderItem
from .calc_distance import calc_distance
from authentication.models import CustomUser


class Booking(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    price_offer = models.DecimalField(max_digits=12, decimal_places=2)
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    shipper = models.ForeignKey(CustomUser, related_name='dispatch', on_delete=models.CASCADE)
    order = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    is_picked = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    destination_address = models.CharField(max_length=255)
    pickup_address = models.CharField(max_length=255)

    def __int__(self):
        return self.pk

    def get_price(self):
        price_per_km = 45
        distance = calc_distance(self.pickup_address, self.destination_address)
        result = distance * price_per_km
        return result
