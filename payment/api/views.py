from rest_framework.response import Response
from rest_framework import status
from .serializers import AccountSerializer, PaymentSerializer
from payment.models import Payment, Account
from order.models import Order
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from paystackapi.transaction import Transaction


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, ])
def create_account(request):
    if request.method == 'POST':
        data = {}
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            data['account_name'] = account.account_name
            data['bank_name'] = account.bank_name
            data['account_number'] = account.account_number
            data['bvn'] = account.bvn
            data['pk'] = account.pk
            data['user'] = request.user.pk
            data['response'] = 'Account created successfully. '
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditAccount(UpdateAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication]


class ViewAccount(RetrieveAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication]


class AllAccounts(ListAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAdminUser, ]
    authentication_classes = [TokenAuthentication]
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, ]
    search_fields = ('user__name', 'user__first_name', )


def make_payment(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = {}
    amount = order.final_price()
    response = Transaction.initialize(amount=amount, email=request.user.email)
    data['reference'] = response['data']['reference']
    data['amount'] = amount
    data['user'] = request.user.pk
    serializer = PaymentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)