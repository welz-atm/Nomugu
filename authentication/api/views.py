from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from authentication.api.serializers import MerchantRegistrationSerializer, ShopperRegistrationSerializer, \
                                           ShipperRegistrationSerializer, ShipperDetailsSerializer, \
                                           PasswordChangeSerializer, CustomUserSerializer
from authentication.models import CustomUser
from rest_framework.authtoken.models import Token


def validate_email(email):
    user = None
    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        return None
    if user is not None:
        return email


@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def register_shopper(request):
    if request.method == 'POST':
        data = {}
        email = request.data.get('email', '0').lower()
        if validate_email(email) is not None:
            data['error_message'] = 'That email is already in use.'
            data['response'] = 'Error'
            return Response(data)

        serializer = ShopperRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            shopper = serializer.save()
            data['first_name'] = shopper.first_name
            data['last_name'] = shopper.last_name
            data['email'] = shopper.email
            data['telephone'] = shopper.telephone
            data['pk'] = shopper.pk
            token = Token.objects.get(user=shopper).key
            data['token'] = token
            data['is_shopper'] = True
            data['response'] = 'Successfully registered new user'
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data['response'] = 'Invalid data'
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def register_merchant(request):
    if request.method == 'POST':
        data = {}
        email = request.data.get('email', '0').lower()
        if validate_email(email) is not None:
            data['error_message'] = 'That email is already in use.'
            data['response'] = 'Error'
            return Response(data)
        serializer = MerchantRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            merchant = serializer.save()
            data['first_name'] = merchant.first_name
            data['last_name'] = merchant.last_name
            data['email'] = merchant.email
            data['telephone'] = merchant.telephone
            data['name'] = merchant.name
            data['state'] = merchant.state
            data['address'] = merchant.address
            data['country'] = merchant.country
            data['bio'] = merchant.bio
            data['pk'] = merchant.pk
            token = Token.objects.get(user=merchant).key
            data['token'] = token
            data['response'] = 'Successfully registered new user'
            return Response(data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def register_shipper(request):
    if request.method == 'POST':
        data = {}
        email = request.data.get('email', '0').lower()

        if validate_email(email) is not None:
            data['error_message'] = 'That email is already in use.'
            data['response'] = 'Error'
            return Response(data)

        serializer = ShipperRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            shipper = serializer.save()
            data['first_name'] = shipper.first_name
            data['last_name'] = shipper.last_name
            data['email'] = shipper.email
            data['telephone'] = shipper.telephone
            data['name'] = shipper.name
            data['state'] = shipper.state
            data['address'] = shipper.address
            data['country'] = shipper.country
            data['bio'] = shipper.bio
            data['pk'] = shipper.pk
            token = Token.objects.get(user=shipper).key
            data['token'] = token
            data['response'] = 'Successfully registered new user'
            return Response(data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST',])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def create_shipper_details(request):
    if request.method == 'POST':
        data = {}
        serializer = ShipperDetailsSerializer(data=request.data)
        if serializer.is_valid():
            details = serializer.save()
            data['engine_number'] = details.engine_number
            data['registration_name'] = details.registration_name
            data['registration_name'] = details.registration_number
            data['year_of_purchase'] = details.year_of_purchase
            data['brand'] = details.brand
            data['vehicle_type'] = details.vehicle_type
            data['license_number'] = details.license_number
            data['price'] = details.price
            data['extra_info'] = details.extra_info
            data['region'] = details.region
            data['unit'] = details.unit
            data['user'] = details.user.pk
            data['response'] = 'Successfully created'
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def edit_profile(request):
    try:
        user = CustomUser.objects.get(user=request.user)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = {}
    if request.user.is_shopper:
        if request.method == 'PUT':
            serializer = ShopperRegistrationSerializer(user)
            if serializer.is_valid():
                shipper = serializer.save()
                data['first_name'] = shipper.first_name
                data['last_name'] = shipper.last_name
                data['email'] = shipper.email
                data['telephone'] = shipper.telephone
                data['pk'] = shipper.pk
                data['response'] = 'Update Successful'
                return Response(data, status=status.HTTP_201_CREATED)

            else:
                return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    elif request.user.is_merchant:
        if request.method == 'PUT':
            serializer = MerchantRegistrationSerializer(user)
            if serializer.is_valid():
                merchant = serializer.save()
                data['first_name'] = merchant.first_name
                data['last_name'] = merchant.last_name
                data['email'] = merchant.email
                data['telephone'] = merchant.telephone
                data['name'] = merchant.name
                data['state'] = merchant.state
                data['address'] = merchant.address
                data['country'] = merchant.country
                data['bio'] = merchant.bio
                data['pk'] = merchant.pk
                data['response'] = 'Successfully registered new user'
                return Response(data, status=status.HTTP_201_CREATED)

            else:
                return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    elif request.user.is_shipper is True:
        if request.method == 'PUT':
            serializer = ShipperRegistrationSerializer(user, data=request.data)
            if serializer.is_valid():
                shipper = serializer.save()
                data['first_name'] = shipper.first_name
                data['last_name'] = shipper.last_name
                data['email'] = shipper.email
                data['telephone'] = shipper.telephone
                data['pk'] = shipper.pk
                data['response'] = 'Successfully registered new user'
                return Response(data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class AllUsers(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser, ]
    authentication_classes = [TokenAuthentication]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', )
    pagination_class = PageNumberPagination


class AllMerchants(ListAPIView):
    queryset = CustomUser.objects.filter(is_merchant=True)
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser, ]
    authentication_classes = [TokenAuthentication]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', )
    ordering_fields = ('state', )
    pagination_class = PageNumberPagination


class AllShippers(ListAPIView):
    queryset = CustomUser.objects.filter(is_shipper=True)
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser, ]
    authentication_classes = [TokenAuthentication]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'state', )
    ordering_fields = ('state', )
    pagination_class = PageNumberPagination


class AllShoppers(ListAPIView):
    queryset = CustomUser.objects.filter(is_shopper=True)
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser, ]
    authentication_classes = [TokenAuthentication]
    filter_backends = (SearchFilter, )
    search_fields = ('name', )
    pagination_class = PageNumberPagination


class ViewUsers(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser, ]
    authentication_classes = [TokenAuthentication]


@api_view(['PUT', ])
@permission_classes((IsAuthenticated, ))
@authentication_classes([TokenAuthentication])
def change_password(request):
    try:
        user = CustomUser.objects.get(pk=request.user.pk)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = {}
    if request.user.is_shopper is True:
        if request.method == 'PUT':
            serializer = PasswordChangeSerializer(user, data=request.data)
            if serializer.is_valid():
                if not request.user.check_password(serializer.data.get('old_password')):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                new_password = serializer.data.get('new_password')
                confirm_password = serializer.data.get('confirm_password')
                if new_password == confirm_password:
                    password = user.set_password(serializer.data.get(new_password))
                    password.save()
                    data['response'] = 'Password changed successfully'
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    data['response'] = 'Passwords must match.'
                    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.user.is_merchant is True:
        if request.method == 'PUT':
            serializer = PasswordChangeSerializer(user, data=request.data)
            if serializer.is_valid():
                if not request.user.check_password(serializer.data.get('old_password')):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                new_password = serializer.data.get('new_password')
                confirm_password = serializer.data.get('confirm_password')
                if new_password == confirm_password:
                    password = user.set_password(serializer.data.get(new_password))
                    password.save()
                    data['response'] = 'Password changed successfully'
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    data['response'] = 'Passwords must match.'
                    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.user.is_shipper is True:
        if request.method == 'PUT':
            serializer = PasswordChangeSerializer(user, data=request.data)
            if serializer.is_valid():
                if not request.user.check_password(serializer.data.get('old_password')):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                new_password = serializer.data.get('new_password')
                confirm_password = serializer.data.get('confirm_password')
                if new_password == confirm_password:
                    password = user.set_password(serializer.data.get(new_password))
                    password.save()
                    data['response'] = 'Password changed successfully'
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    data['response'] = 'Passwords must match.'
                    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class ObtainAuthTokenView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        data = {}
        email = request.POST.get('email')
        password = request.POST.get('password')
        account = authenticate(email=email, password=password)
        if account:
            try:
                token = Token.objects.get(user=account).key
            except Token.DoesNotExist:
                token = Token.objects.create(user=account)
            data['response'] = 'Successfully authenticated.'
            data['pk'] = account.pk
            data['email'] = email.lower()
            data['token'] = token.key
        else:
            data['response'] = 'Error'
            data['error_message'] = 'Invalid credentials'
        return Response(data)