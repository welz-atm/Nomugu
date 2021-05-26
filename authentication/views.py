from django.shortcuts import render, redirect, HttpResponse
from .models import CustomUser, Shipper
from payment.models import Account
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib import messages
from .forms import ShopperRegisterForm, ShopperEditForm, MerchantRegisterForm, MerchantEditForm, ShipperForm, \
                                                           ShipperRegisterForm, ShipperEditForm, ChangePasswordForm
from django.contrib.auth.decorators import login_required
from django_countries import countries
from NoMugu.settings import EMAIL_HOST_USER
from .task import email_password_request, welcome_message, password_changed


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        credential = authenticate(request, username=email, password=password)
        if credential is not None:
            user = CustomUser.objects.get(email=email)
            if user.is_authenticated and user.is_shopper:
                login(request, credential)
                return redirect('home')
            if user.is_authenticated and user.is_merchant:
                login(request, credential)
                return redirect('dashboard')
            if user.is_authenticated and user.is_admin:
                login(request, credential)
                return redirect('dashboard')
            if user.is_authenticated and user.is_shipper:
                login(request, credential)
                return redirect('dashboard')
        else:
            messages.success(request, 'Invalid Username/Password')
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    return redirect('home')


def register_shopper(request):
    if request.method == 'POST':
        form = ShopperRegisterForm(request.POST)
        if form.is_valid():
            shopper = form.save(commit=False)
            shopper.is_shopper = True
            shopper.save()
            welcome_message.delay(shopper.pk)
            login(request, shopper, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')

    else:
        form = ShopperRegisterForm()
    context = {'form': form}
    return render(request, 'register_shopper.html', context)


def register_merchant(request):
    if request.method == 'POST':
        form = MerchantRegisterForm(request.POST)
        if form.is_valid():
            merchant = form.save(commit=False)
            merchant.is_merchant = True
            merchant.save()
            welcome_message.delay(merchant.pk)
            login(request, merchant, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('create_account')

    else:
        form = MerchantRegisterForm()

    context = {
        'form': form,
        'countries': countries
    }
    return render(request, 'register_merchant.html', context)


def register_shipper(request):
    if request.method == 'POST':
        form = ShipperRegisterForm(request.POST)
        if form.is_valid():
            shipper = form.save(commit=False)
            shipper.is_shipper = True
            shipper.save()
            welcome_message.delay(shipper.pk)
            login(request, shipper, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('create_shipper_details')
    else:
        form = ShipperRegisterForm()
    context = {
        'form': form,
        'countries': countries
    }
    return render(request, 'register_shipper.html', context)


def edit_user(request):
    user = CustomUser.objects.get(pk=request.user.pk)
    if request.method == 'POST' and request.user.is_merchant:
        form = MerchantEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update successfully')
            return redirect('settings')
        else:
            form = MerchantEditForm(instance=user)
        context = {
            'form': form,
            'user': user
            }
        return render(request, 'account_settings.html', context)
    if request.method == 'POST' and request.user.is_shipper:
        shipper = Shipper.objects.get(user=user)
        form = ShipperEditForm(request.POST, instance=user)
        detail_form = ShipperForm(request.POST, instance=shipper)
        if form.is_valid() and detail_form.is_valid():
            form.save()
            detail_form.user = request.user
            detail_form.save()
            messages.success(request, 'Update successfully')
            return redirect('settings')
        else:
            form = ShipperEditForm(instance=shipper)
            detail_form = ShipperForm(instance=shipper)
        context = {
            'form': form,
            'user': user,
            'detail_form': detail_form,
            'shipper': shipper
            }
        return render(request, 'account_settings.html', context)
    if request.method == 'POST' and request.user.is_shopper:
        form = ShopperEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update successfully')
            return redirect('settings')
        else:
            form = ShopperEditForm(instance=user)
        context = {
            'form': form,
            'user': user,
            }
        return render(request, 'account_settings.html', context)

    else:
        return HttpResponse('You do not have access to do this')


def create_shipper_details(request):
    if request.method == 'POST':
        form = ShipperForm(request.POST)
        if form.is_valid():
            shipper = form.save(commit=False)
            shipper.user = request.user
            shipper.save()
            return redirect('create_account')
    else:
        form = ShipperForm()
    context = {
        'form': form
    }
    return render(request, 'create_shipper_details.html', context)


def edit_shipper_details(request):
    shipper = Shipper.objects.get(pk=request.user.pk)
    if request.method == 'POST':
        form = ShipperForm(request.POST, instance=shipper)
        if form.is_valid():
            shipper_form = form.save(commit=False)
            shipper_form.user = request.user
            shipper_form.save()
            return redirect('settings')
    else:
        form = ShipperForm(instance=shipper)
    context = {
        'form': form,
        'shipper': shipper
    }
    return render(request, 'create_shipper_details.html', context)


@login_required()
def profile(request):
    if request.user.is_shopper is True:
        if request.method == 'POST':
            form = ShopperEditForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('profile')
        else:
            form = ShopperEditForm(instance=request.user)
        context = {'form': form}
        return render(request, 'profile.html', context)
    elif request.user.is_merchant is True:
        if request.method == 'POST':
            form = MerchantEditForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('profile')
        else:
            form = MerchantEditForm(instance=request.user)
        context = {'form': form}
        return render(request, 'profile.html', context)
    elif request.user.is_shipper is True:
        if request.method == 'POST':
            form = ShipperEditForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('profile')
        else:
            form = ShipperEditForm(instance=request.user)
        context = {'form': form}
        return render(request, 'profile.html', context)


def view_profile(request, pk):
    user = CustomUser.objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'view_profile.html', context)


def account_setting(request):
    context = {
        'countries': countries
    }
    return render(request, 'account_settings.html', context)


def reset_password_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.exists():
                email_password_request.delay(user.pk)
                return redirect("reset_done")
    else:
        form = PasswordResetForm()
    context = {
           'form': form
       }
    return render(request, 'password_reset.html', context)


@login_required()
def change_password(request):
    if request.method == 'POST':
        if request.user.is_shopper is True:
            form = ChangePasswordForm(data=request.POST, user=request.user)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password changed successfully')
                password_changed.delay(user.pk)
                return redirect('settings')
        elif request.user.is_merchant is True:
            form = ChangePasswordForm(data=request.POST, user=request.user)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password changed successfully')
                password_changed.delay(user.pk)
                return redirect('settings')
        elif request.user.is_shipper is True:
            form = ChangePasswordForm(data=request.POST, user=request.user)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password changed successfully')
                password_changed.delay(user.pk)
                return redirect('settings')

    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'account_settings.html', context)