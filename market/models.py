from django.db import models
from django_resized import ResizedImageField
from product.models import Category


class Market(models.Model):
    name = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    categories = models.ManyToManyField(Category)
    image = ResizedImageField(size=[500, 500], upload_to='media', null=True, blank=True)
    address = models.CharField(max_length=140, default='463 Ikorodu Road, Ketu, Lagos')

    def __str__(self):
        return self.name
