from .models import Product
import django_filters

processor_choices = (('Intel Core', 'Intel Core'), ('Intel Celeron', 'Intel Celeron'), ('Intel Xeon', 'Intel Xeon'),
                     ('Intel Core i3', 'Intel Core i3'), ('Intel Core i5', 'Intel Core i5'),
                     ('Intel Core i7', 'Intel Core i7'), ('Intel Core i9', 'Intel Core i9'), ('AMD Ryzen 3', 'AMD Ryzen 3'),
                     ('AMD Ryzen 5', 'AMD Ryzen 5'), ('AMD Ryzen 7', 'AMD Ryzen 7')
)


class ComputerFilter(django_filters.FilterSet):
    brand = django_filters.ModelChoiceFilter(queryset=Product.objects.filter(name='Laptop'))
    processor = django_filters.ChoiceFilter(choices=processor_choices)
    ram = django_filters.ChoiceFilter(field_name='title', lookup_expr='contains')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['brand', 'price', 'title']


class NetworkFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(field_name='brand', lookup_expr='contains')
    processor = django_filters.CharFilter(field_name='brand', lookup_expr='contains')
    ram = django_filters.CharFilter(field_name='title', lookup_expr='contains')
    series = django_filters.CharFilter(field_name='title', lookup_expr='contains')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['brand', 'price', 'title']


class PhonesFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(field_name='brand', lookup_expr='contains')
    ram = django_filters.CharFilter(field_name='title', lookup_expr='contains')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['brand', 'price', 'title']


class FashionFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(field_name='brand', lookup_expr='contains')
    color = django_filters.CharFilter(field_name='color', lookup_expr='contains')
    size = django_filters.CharFilter(field_name='size', lookup_expr='contains')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['brand', 'price', 'title']


class ElectronicsFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(field_name='brand', lookup_expr='exact')
    color = django_filters.CharFilter(field_name='color', lookup_expr='exact')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['brand', 'price', 'title']


class AcFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(field_name='brand', lookup_expr='contains')
    horsepower = django_filters.CharFilter(field_name='title', lookup_expr='contains')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['brand', 'price', 'title']


class FruitFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='title', lookup_expr='contains')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['brand', 'price', 'title']


class FurnitureFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(field_name='brand', lookup_expr='contains')
    type = django_filters.CharFilter(field_name='title', lookup_expr='contains')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['brand', 'price', 'title']


class HomeApplianceFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(field_name='brand', lookup_expr='contains')
    type = django_filters.CharFilter(field_name='title', lookup_expr='contains')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['brand', 'price', 'title']


class KitchenApplianceFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(field_name='brand', lookup_expr='contains')
    type = django_filters.CharFilter(field_name='title', lookup_expr='contains')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['brand', 'price', 'title']


class ConstructionFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(field_name='brand', lookup_expr='contains')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['brand', 'price', 'title']
