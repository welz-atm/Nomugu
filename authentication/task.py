from django.core.mail import send_mail
from .models import CustomUser
from celery.decorators import task
from django.template.loader import render_to_string
from NoMugu.settings import EMAIL_HOST_USER


@task(name='welcome_message')
def welcome_message(user_id):
    user_id = user_id
    if user_id:
        user = CustomUser.objects.get(pk=user_id)
        subject = 'Welcome to Nomugu'
        template = "welcome_message.txt"
        message_context = {
            "email": user.email,
            'domain': '127.0.0.1:8000',
            'site_name': 'NoMugu',
            "user": user,
            'protocol': 'http',
        }
        message = render_to_string(template, message_context)
        try:
            send_mail(subject, message, EMAIL_HOST_USER, [user.email], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
    else:
        return None


@task(name='email_password_request')
def email_password_request(user_id):
    user = CustomUser.objects.get(pk=user_id)
    subject = 'Password Rest Requested'
    template = "password_reset.txt"
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
