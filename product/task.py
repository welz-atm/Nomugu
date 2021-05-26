from django.core.mail import send_mail
from .models import Product
from celery.decorators import task
from django.template.loader import render_to_string
from NoMugu.settings import EMAIL_HOST_USER


@task(name='product_viewed')
def product_viewed(product_id):
    product = Product.objects.get(pk=product_id)
    subject = 'Someone Viewed your product'
    template = "product_viewed.txt"
    message_context = {
        "email": product.merchant.email,
        "product": product,
    }
    message = render_to_string(template, message_context)
    try:
        send_mail(subject, message, EMAIL_HOST_USER, [product.merchant.email], fail_silently=False)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')


@task(name='product_added')
def new_product_added(product_id):
    product = Product.objects.get(pk=product_id)
    subject = 'New Product Added.({})'.format(product.title)
    template = "product_added.txt"
    message_context = {
        "email": product.merchant.email,
        "product": product,
    }
    message = render_to_string(template, message_context)
    try:
        send_mail(subject, message, EMAIL_HOST_USER, [product.merchant.email], fail_silently=False)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')


@task(name='password_changed')
def password_changed(user_id):
    user = CustomUser.objects.get(pk=user_id)
    subject = 'Password Reset Successful'
    template = "password_changed.txt"
    message_context = {
        "email": user.email,
        'domain': '127.0.0.1:8000',
        'site_name': 'NoMugu',
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "user": user,
        'token': default_token_generator.make_token(user),
        'protocol': 'http',
    }
    message = render_to_string(template, message_context)
    try:
        send_mail(subject, message, EMAIL_HOST_USER, [user.email], fail_silently=False)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
