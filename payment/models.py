from django.db import models
from authentication.models import CustomUser
from order.models import Order


class Account(models.Model):
    account_name = models.CharField(max_length=150)
    bank_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_created = models.BooleanField(default=False)

    def __str__(self):
        return self.account_name


class Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment_date = models.DateTimeField(null=True, blank=True)
    reference = models.CharField(max_length=50)
    status = models.CharField(max_length=50, null=True, blank=True)
    channel = models.CharField(max_length=50, null=True, blank=True)
    card_type = models.CharField(max_length=50, null=True, blank=True)
    bank_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


