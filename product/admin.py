from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'quantity', 'description', 'price', 'category', 'merchant')
    list_filter = ('merchant', 'price', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.unregister(Group)



