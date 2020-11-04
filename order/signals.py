from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.db.models import Max
from .models import Invoices


@receiver(pre_save, sender=Invoices)
def create_invoice_no(sender, instance, **kwargs):
    largest = Invoices.objects.all().aggregate(Max("number"))['number__max']
    if largest:
        instance.number = largest + 1
    else:
        instance.number = 10000000