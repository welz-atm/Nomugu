from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import OrderItem, Order, Invoices
from .forms import OrderItemForm, OrderCreateForm
from authentication.decorators import merchant_required, shipper_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from product.models import Product
import datetime


@login_required()
def add_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order_item, created = OrderItem.objects.get_or_create(product=product, user=request.user)
    orders = Order.objects.filter(user=request.user, ordered=False)
    if orders.exists():
        order = orders[0]
        if order.products.filter(product=product).exists():
            order_item.quantity += 1
            order_item.save()
            return redirect('my_cart')
        else:
            order.products.add(order_item)
            return redirect('my_cart')

    else:
        order = Order.objects.create(
            user=request.user)
        order.products.add(order_item)
        return redirect("my_cart")


@login_required()
def my_cart(request):
    try:
        order = Order.objects.get(user=request.user, ordered=False)
    except Order.DoesNotExist:
        return render(request, 'no_cart.html', {})
    if request.method == 'POST':
        form = OrderCreateForm(request.POST, instance=order)
        if form.is_valid():
            created_form = form.save(commit=False)
            created_form.detail_created = True
            created_form.user = request.user
            created_form.save()
            redirect('my_cart')
    else:
        form = OrderCreateForm(instance=order)

    context = {
        'order': order,
        'form': form,
    }
    return render(request, 'cart.html', context)


@login_required()
def remove_from_cart(request, pk):
    ordered_item = get_object_or_404(OrderItem, pk=pk)
    ordered_item.delete()
    return redirect('my_cart')


@login_required()
def update_cart(request, pk):
    order = OrderItem.objects.get(pk=pk)
    if request.method == 'POST':
        form = OrderItemForm(request.POST, instance=order)
        if form.is_valid():
            updated_item = form.save(commit=False)
            updated_item.user = request.user
            updated_item.save()
            return redirect('my_cart')
    else:
        form = OrderItemForm(instance=order)
    context = {
        'form': form,
        'order': order
    }
    return render(request, 'update_cart.html', context)


def cart_count(request):
    order_count = OrderItem.objects.filter(user=request.user).count()
    context = {
        'order_count': order_count
    }
    return render(request, 'cart.html', context)


def my_orders(request):
    orders = OrderItem.objects.filter(product__merchant=request.user, ordered=True).order_by('-order_date')
    context = {
               'orders': orders
              }

    return render(request, 'my_orders.html', context)


def delivered_orders(request):
    if request.user.is_shipper:
        orders = OrderItem.objects.filter(shipper=request.user, delivered=True).order_by('-order_date')
        context = {
            'orders': orders
        }
        return render(request, 'delivered_orders.html', context)
    else:
        raise PermissionDenied


def picked_up_orders(request):
    if request.user.is_shipper:
        orders = OrderItem.objects.filter(shipper=request.user, picked=True).order_by('-order_date')
        context = {
            'orders': orders
        }
        return render(request, 'picked_up_orders.html', context)
    else:
        raise PermissionDenied


@login_required()
def available_pickup(request):
    if request.user.is_shipper:
        pick_ups = OrderItem.objects.filter(ordered=True, picked=False).select_related('user', 'product')
        context = {
            'pick_ups': pick_ups
        }
        return render(request, 'available_pickup.html', context)
    elif request.user.is_admin:
        pick_ups = OrderItem.objects.filter(ordered=True, picked=False).select_related('user', 'product')
        context = {
            'pick_ups': pick_ups
        }
        return render(request, 'available_pickup.html', context)
    elif request.user.is_merchant:
        pick_ups = OrderItem.objects.filter(ordered=True, picked=False).select_related('user', 'product')
        context = {
            'pick_ups': pick_ups
        }
        return render(request, 'available_pickup.html', context)
    else:
        raise PermissionDenied


@shipper_required()
def select_order_pickup(request, pk):
    order_item = get_object_or_404(OrderItem, pk=pk)
    if request.user.is_shipper:
        if order_item.picked is False:
            order_item.picked = True
            order_item.shipper = request.user
            order_item.save()
            context = {
              'order_item': order_item
            }
            return render(request, 'pickup_order.html', context)
        else:
            messages.success(request, 'This order has been selected.')
            return redirect('available_pickup')
    else:
        raise PermissionDenied


def view_order(request, pk):
    order_item = OrderItem.objects.get(pk=pk)
    if request.user.is_shipper:
        order = Order.objects.get(user=order_item.user.pk)
        orders = order.products.filter(product=order_item.product.pk)
        context = {
           'order_item': order_item,
           'orders': orders
        }
        return render(request, 'view_order.html', context)
    else:
        raise PermissionDenied


@shipper_required()
def product_delivered(request, pk):
    order_item = get_object_or_404(OrderItem, pk=pk)
    if order_item.shipper == request.user:
        order_item.delivered = True
        order_item.save()
        context = {
            'order_item': order_item
        }
        return render(request, 'pickup_order.html', context)
    else:
        return HttpResponse('You are not allowed')


@login_required()
def generate_invoice(request, pk):
    order = get_object_or_404(Order, pk=pk)
    invoice = Invoices.objects.create(owner=order.first_name, order=order)
    context = {
               'invoice': invoice
              }
    return render(request, 'invoice.html', context)


@login_required()
def invoice_list(request, pk):
    order = get_object_or_404(OrderItem, pk=pk)
    invoice = Invoices.objects.filter(order=order.product.merchant).select_related('Order', 'OrderItem')
    context = {
               'invoice': invoice
              }

    return render(request, 'all_invoices.html', context)