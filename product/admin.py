from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'description', 'price', 'category', 'merchant')
    list_filter = ('merchant', 'price', 'category')


admin.site.register(Product, ProductAdmin)
admin.site.unregister(Group)



