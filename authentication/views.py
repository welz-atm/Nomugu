from django.shortcuts import render, redirect, HttpResponse
from .models import CustomUser, Shipper
from payment.models import Account
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import ShopperRegisterForm, ShopperEditForm, MerchantRegisterForm, MerchantEditForm, ShipperForm, \
                                                           ShipperRegisterForm, ShipperEditForm
from django.contrib.auth.decorators import login_required


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
            elif user.is_authenticated and user.is_merchant:
                login(request, credential)
                return redirect('dashboard')
            elif user.is_authenticated and user.is_admin:
                login(request, credential)
                return redirect('dashboard')
            elif user.is_authenticated and user.is_shipper:
                login(request, credential)
                return redirect('dashboard')
            else:
                messages.success(request, 'Please confirm your login details ')
                return redirect('login')
        else:
            messages.success(request, 'Invalid Username/Password')
            return redirect('login')
    else:
        return render(request, 'login_user.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have logged out successfully.')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = ShopperRegisterForm(request.POST)
        if form.is_valid():
            shopper = form.save(commit=False)
            shopper.is_shopper = True
            shopper.save()
            login(request, shopper, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')

    else:
        form = ShopperRegisterForm()
    context = {'form': form}
    return render(request, 'register_user.html', context)


def register_merchant(request):
    if request.method == 'POST':
        form = MerchantRegisterForm(request.POST)
        if form.is_valid():
            merchant = form.save(commit=False)
            merchant.is_merchant = True
            merchant.save()
            login(request, merchant, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, 'You have registered successfully.')
            return redirect('create_account')

    else:
        form = MerchantRegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'register_merchant.html', context)


def register_shipper(request):
    if request.method == 'POST':
        form = ShipperRegisterForm(request.POST)
        if form.is_valid():
            shipper = form.save(commit=False)
            shipper.is_shipper = True
            shipper.save()
            login(request, shipper, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, 'You have registered successfully')
            return redirect('create_shipper_details')
    else:
        form = ShipperRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'register_shipper.html', context)


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


@login_required()
def profile(request):
    if request.user.is_shopper is True:
        if request.method == 'POST':
            form = ShopperEditForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Update successful.')
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
                messages.success(request, 'Update successful.')
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
                messages.success(request, 'Update successful.')
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


@login_required()
def change_password(request):
    if request.user.is_shopper is True:
        if request.method == 'POST':
            form = PasswordChangeForm(data=request.POST, user=request.user)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password changed successfully')
                return redirect('dashboard')

        else:
            form = PasswordChangeForm(user=request.user)
        context = {'form': form}
        return render(request, 'change_password.html', context)
    elif request.user.is_merchant is True:
        if request.method == 'POST':
            form = PasswordChangeForm(data=request.POST, user=request.user)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password changed successfully')
                return redirect('dashboard')

        else:
            form = PasswordChangeForm(user=request.user)
        context = {'form': form}
        return render(request, 'change_password.html', context)
    elif request.user.is_shipper is True:
        if request.method == 'POST':
            form = PasswordChangeForm(data=request.POST, user=request.user)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password changed successfully')
                return redirect('dashboard')

        else:
            form = PasswordChangeForm(user=request.user)
        context = {'form': form}
        return render(request, 'change_password.html', context)
    else:
        return HttpResponse('You do not have access to do this')