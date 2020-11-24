from django.db import models
from authentication.models import CustomUser
from order.models import Order


Banks = (
    ('Access Bank', 'Access Bank'),
    ('Citibank', 'Citibank'),
    ('Diamond Bank', 'Diamond Bank'),
    ('Ecobank Nigeria', 'Ecobank Nigeria'),
    ('Fidelity Bank Nigeria', 'Fidelity Bank Nigeria'),
    ('First Bank of Nigeria', 'First Bank of Nigeria'),
    ('First City Monument Bank', 'First City Monument Bank'),
    ('Guaranty Trust Bank', 'Guaranty Trust Bank'),
    ('Heritage Bank Plc', 'Heritage Bank Plc'),
    ('Jaiz Bank', 'Jaiz Bank'),
    ('Keystone Bank Limited', 'Keystone Bank Limited'),
    ('Providus Bank Plc', 'Providus Bank Plc'),
    ('Polaris Bank', 'Polaris Bank'),
    ('Stanbic IBTC Bank Nigeria Limited', 'Stanbic IBTC Bank Nigeria Limited'),
    ('Standard Bank', 'Standard Bank'),
    ('Standard Chartered Bank', 'Standard Chartered Bank'),
    ('Sterling Bank', 'Sterling Bank'),
    ('Suntrust Bank Nigeria Limited', 'Suntrust Bank Nigeria Limited'),
    ('Union Bank of Nigeria', 'Union Bank of Nigeria'),
    ('United Bank for Africa', 'United Bank for Africa'),
    ('Unity Bank Plc', 'Unity Bank Plc'),
    ('Wema Bank', 'Wema Bank'),
    ('Zenith Bank', 'Zenith Bank')
)


class Account(models.Model):
    account_name = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50, null=True, blank=True, choices=Banks)
    account_number = models.IntegerField()
    account_id = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_created = models.BooleanField(default=False)
    salary = models.IntegerField(null=True, blank=True)
    employer = models.CharField(max_length=255, null=True, blank=True)
    employer_address = models.CharField(max_length=300, null=True, blank=True)
    job_role = models.CharField(max_length=300, null=True, blank=True)

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


