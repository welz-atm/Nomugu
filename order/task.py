from django.core.mail import send_mail
from .models import Order
from celery.decorators import task
from django.template.loader import render_to_string
from NoMugu.settings import EMAIL_HOST_USER


@task(name='order_selected')
def order_selected(user_id, order_id):
    user = CustomUser.objects.get(pk=user_id)
    order = OrderItem.objects.get(pk=order_id)
    subject = 'Order has been selected'
    template = "order_selected.txt"
    message_context = {
        'order': order,
        'user': user
    }
    message = render_to_string(template, message_context)
    try:
        send_mail(subject, message, EMAIL_HOST_USER, [order.user.email], fail_silently=False)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')


@task(name='order_picked')
def order_picked(user_id, order_id):
    user = CustomUser.objects.get(pk=user_id)
    order = OrderItem.objects.get(pk=order_id)
    subject = 'Order has been picked'
    template = "order_picked.txt"
    message_context = {
        'order': order,
        'user': user
    }
    message = render_to_string(template, message_context)
    try:
        send_mail(subject, message, EMAIL_HOST_USER, [order.user.email], fail_silently=False)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')


@task(name='product_disapproved')
def product_disapproved(order_id):
    order = OrderItem.objects.get(pk=order_id)
    product = Product.objects.get(pk=order.product.pk)
    subject = 'Product disapproved by customer'
    template = "product_disapproved.txt"
    message_context = {
        'order': order,
        'user': user
    }
    message = render_to_string(template, message_context)
    try:
        send_mail(subject, message, EMAIL_HOST_USER, [product.merchant.email], fail_silently=False)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')


@task(name='order_delivered')
def order_delivered(order_id):
    order = OrderItem.objects.get(pk=order_id)
    product = Product.objects.get(pk=order.product.pk)
    subject = 'Product delivered'
    template = "product_delivered.txt"
    message_context = {
        'order': order,
        'user': user
    }
    message = render_to_string(template, message_context)
    try:
        send_mail(subject, message, EMAIL_HOST_USER, [product.merchant.email], fail_silently=False)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
