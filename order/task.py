from django.core.mail import send_mail
from .models import Order
from authentication.models import CustomUser
from celery.decorators import task
from django.template.loader import render_to_string
from NoMugu.settings import EMAIL_HOST_USER
from twilio.rest import Client


@task(name='order_selected')
def order_selected(user_id, order_id):
    user = CustomUser.objects.get(pk=user_id)
    order = OrderItem.objects.get(pk=order_id)
    subject = 'Order has been selected'
    template = "order_selected.txt"
    context = {
        'order': order,
        'user': user
    }
    message = render_to_string(template, context)
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
    context = {
        'order': order,
        'user': user
    }
    message = render_to_string(template, context)
    try:
        send_mail(subject, message, EMAIL_HOST_USER, [order.user.email], fail_silently=False)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')


@task(name='order_picked')
def send_text_for_order_picked(order_id):
    order = OrderItem.objects.get(pk=order_id)
    message_to_broadcast = ("Your order is on its way. Its picked up by {}. You can reach him at {}."
                            .format(order.shipper.first_name, order.shipper.telephone))
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    client.messages.create(to=order.user.telephone, from_=settings.TWILIO_NUMBER, body=message_to_broadcast)


@task(name='product_disapproved')
def product_disapproved(order_id):
    order = OrderItem.objects.get(pk=order_id)
    product = Product.objects.get(pk=order.product.pk)
    subject = 'Product disapproved by customer'
    template = "product_disapproved.txt"
    context = {
        'order': order,
        'user': user
    }
    message = render_to_string(template, context)
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
    context = {
        'order': order,
        'user': user
    }
    message = render_to_string(template, context)
    try:
        send_mail(subject, message, EMAIL_HOST_USER, [product.merchant.email], fail_silently=False)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
