from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from product.api.serializers import ProductSerializer
from product.models import Product, Category


@api_view(['POST',])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def register_product(request):
    if request.method == 'POST':
        data = {}
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save(merchant=request.user)
            data['name'] = product.name
            data['category'] = product.category
            data['title'] = product.title
            data['brand'] = product.brand
            data['quantity'] = product.quantity
            data['weight'] = product.weight
            data['price'] = product.price
            data['unit'] = product.unit
            data['image'] = product.image
            data['extra_info'] = product.price
            data['description'] = product.description
            data['merchant'] = product.user.pk
            data['response'] = 'Successful created'
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
@permission_classes((IsAuthenticated, ))
def edit_product(request):
    try:
        product = Product.objects.get(user=request.user).select_related('merchant')
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if product.merchant == request.user:
        if request.method == 'PUT':
            serializer = ProductSerializer(product)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET',])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def my_product(request):
    products = Product.objects.filter(merchant=request.user).select_related('merchant')
    if request.method == 'GET':
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AllProducts(ListAPIView):
    queryset = Product.objects.all().select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'title', )
    pagination_class = PageNumberPagination


class ViewProduct(RetrieveAPIView):
    queryset = Product.objects.all().select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer


class AllLaptops(ListAPIView):
    queryset = Product.objects.filter(name='Laptop').select_related('merchant', 'category')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllServers(ListAPIView):
    queryset = Product.objects.filter(name='Server').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllNetworkDevices(ListAPIView):
    queryset = Product.objects.filter(name='Networking').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllDesktops(ListAPIView):
    queryset = Product.objects.filter(name='Laptop').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllAndroids(ListAPIView):
    queryset = Product.objects.filter(name='Android').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllIos(ListAPIView):
    queryset = Product.objects.filter(name='IOS').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllClothings(ListAPIView):
    queryset = Product.objects.filter(name='Laptop').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllFootwears(ListAPIView):
    queryset = Product.objects.filter(name='Footwear').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllFragrances(ListAPIView):
    queryset = Product.objects.filter(name='Fragrance').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllWatches(ListAPIView):
    queryset = Product.objects.filter(name='Watch').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllFabrics(ListAPIView):
    queryset = Product.objects.filter(name='Fabric').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllTelevisions(ListAPIView):
    queryset = Product.objects.filter(name='Television').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllAirConditioners(ListAPIView):
    queryset = Product.objects.filter(name='Air Conditioner').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllAudio(ListAPIView):
    queryset = Product.objects.filter(name='Audio').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllRefrigerators(ListAPIView):
    queryset = Product.objects.filter(name='Refrigerator').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllFreezers(ListAPIView):
    queryset = Product.objects.filter(name='Freezer').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllCookers(ListAPIView):
    queryset = Product.objects.filter(name='Cooker').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllMicrowaves(ListAPIView):
    queryset = Product.objects.filter(name='Microwave').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllDispensers(ListAPIView):
    queryset = Product.objects.filter(name='Dispenser').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllBlenders(ListAPIView):
    queryset = Product.objects.filter(name='Blender').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllKettles(ListAPIView):
    queryset = Product.objects.filter(name='Kettle').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllWashers(ListAPIView):
    queryset = Product.objects.filter(name='Washer').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllFurniture(ListAPIView):
    queryset = Product.objects.filter(name='Furniture').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllFans(ListAPIView):
    queryset = Product.objects.filter(name='Fan').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination


class AllBeds(ListAPIView):
    queryset = Product.objects.filter(name='Bed').select_related('merchant')
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('brand', 'title__contains', 'price__lte', 'price__gte', )
    ordering_fields = ('brand', 'price', )
    pagination_class = PageNumberPagination