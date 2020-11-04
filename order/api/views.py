from rest_framework.response import Response
from rest_framework import status
from order.models import OrderItem, Order, Invoices
from .serializers import OrderSerializer, OrderItemSerializer
from product.models import Product


def add_cart(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = {}
    data['product'] = product
    data['user'] = request.user.pk
    serializer = OrderItemSerializer(data=data)
    if serializer.is_valid():
        order_item = serializer.save()
        orders = Order.objects.filter(user=request.user)
        if orders.exists():
            order = orders[0]
            if order.product.filter(product=product).exists():
                order_item.quantity += 1
                order_item.save()
                return Response(status=status.HTTP_200_OK)
            else:
                order.product.add(order_item)
                return Response(status=status.HTTP_200_OK)

        else:
            data = {}
            data['user'] = request.user.pk
            serializer = OrderSerializer(data=data)
            order = serializer.save()
            order.product.add(order_item)
            order.save()
            data['response'] = 'Product added to cart successfully'
            return Response(status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)