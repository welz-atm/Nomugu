from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'category', 'title', 'brand', 'quantity', 'weight', 'unit', 'image', 'price', 'shipping',
                  'description', 'merchant', )