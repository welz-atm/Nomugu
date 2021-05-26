from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.core.exceptions import PermissionDenied
from .forms import AccountForm
from .models import Account, Payment
from product.models import Product
from order.models import Order, OrderItem
from paystackapi.transaction import Transaction
from paystackapi.verification import Verification
from paystackapi.subaccount import SubAccount
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.conf import settings
from paystackapi.paystack import Paystack
from paystackapi.misc import Misc


def create_account(request):
    list_banks = []
    banks = Misc.list_banks()
    for bank in banks['data']:
        list_banks.append(bank)
    if request.method == 'POST' and request.user.is_shipper or request.user.is_merchant:
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            paystack = Paystack(secret_key=settings.PAYSTACK_SECRET_KEY)
            try:
                response = paystack.verification.verify_account(account_number=account.account_number,
                                                                bank_code=account.bank_name)
            except paystack.DoesNotExist:
                render(request, '404.html')
            if response['status']:
                account.user = request.user
                account.is_created = True
                account.save()
                return redirect('dashboard')
    elif request.method == 'POST' and request.user.is_shopper:
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            paystack = Paystack(secret_key=settings.PAYSTACK_SECRET_KEY)
            response = paystack.verification.verify_account(account_number=account.account_number,
                                                            bank_code=account.bank_name)
            if response['status']:
                account.user = request.user
                account.is_created = True
                account.save()
                return redirect('home')
    else:
        form = AccountForm()
    context = {
        'form': form,
        'list_banks': list_banks
        }
    return render(request, 'create_account.html', context)


@login_required()
def edit_account(request, pk):
    list_banks = []
    banks = Misc.list_banks()
    for bank in banks['data']:
        list_banks.append(bank)
    account = Account.objects.get(pk=pk)
    if account.user == request.user:
        if request.method == 'POST' and request.user.is_merchant or request.user.is_shipper:
            form = AccountForm(request.POST, instance=account)
            if form.is_valid():
                account = form.save(commit=False)
                account.user = request.user
                account.is_created = True
                account.save()
                return redirect('account_details')
        elif request.method == 'POST' and request.user.is_shopper:
            form = AccountForm(request.POST, instance=account)
            if form.is_valid():
                account = form.save(commit=False)
                account.user = request.user
                account.is_created = True
                account.save()
                return redirect('account_details')
        else:
            form = AccountForm(instance=account)
        context = {
            'form': form,
            'account': account,
            'list_banks': list_banks
        }
        return render(request, 'edit_account.html', context)
    else:
        raise PermmissionDenied


def account_details(request):
    if request.user.is_shipper or request.user.is_merchant or request.user.is_shopper:
        account = get_object_or_404(Account, pk=request.user.pk)
        context = {
            'account': account
        }
        return render(request, 'account_details.html', context)

    return HttpResponse('You do not have access to this page')


def make_payment(request, pk):
    order = get_object_or_404(Order, pk=pk)
    amount = order.final_price() * 100
    paystack = Paystack(secret_key=settings.PAYSTACK_SECRET_KEY)
    response = paystack.transaction.initialize(amount=amount, email=request.user.email,
                                               callback_url='http://localhost:8000/payment/my_payment/')
    url = response['data']['authorization_url']
    reference = response['data']['reference']
    amount_formatted = amount/100
    payment = Payment.objects.create(user=request.user, reference=reference, amount=amount_formatted, order=order)
    payment.save()
    return redirect(url)


def payment_page(request):
    orders = OrderItem.objects.filter(product__merchant=request.user, ordered=True).select_related('user').\
                                     order_by('-order_date')
    context = {
        'orders': orders
    }
    return render(request, 'payment_verification.html', context)


@login_required()
def success_page(request):
    return render(request, 'success.html', {})


@login_required()
def my_payment(request):
    try:
        order = Order.objects.get(user=request.user, ordered=False)
    except Order.DoesNotExist:
        payments = Payment.objects.filter(user=request.user).order_by('-payment_date').select_related('user', 'order')
        if payments.exists():
            paginator = Paginator(payments, 10)
            page_number = request.GET.get('page')
            payments = paginator.get_page(page_number)
        context = {
            'payments': payments
        }
        return render(request, 'payment_verification.html', context)

    payments = Payment.objects.filter(order=order).order_by('payment_date').select_related('user', 'order')
    payment = payments[0]
    paystack = Paystack(secret_key=settings.PAYSTACK_SECRET_KEY)
    response = paystack.transaction.verify(reference=payment.reference)
    payment.user = request.user
    payment.amount = response['data']['amount']
    payment.payment_date = response['data']['transaction_date']
    payment.status = response['data']['status']
    payment.channel = response['data']['channel']
    payment.save()
    order_items = order.products.all()
    order_items.update(ordered=True)
    for item in order_items:
        product = Product.objects.get(pk=item.product.pk)
        product.quantity = product.quantity - item.quantity
        product.save()
        item.save()
    order.ordered = True
    order.save()
    context = {
      'payment': payment,
      'payments': payments
    }
    return render(request, 'payment_verifications.html', context)