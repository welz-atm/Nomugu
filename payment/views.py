from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import AccountForm
from .models import Account, Payment
from order.models import Order, OrderItem
from paystackapi.transaction import Transaction
from django.contrib.auth.decorators import login_required


def create_account(request):
    if request.user.is_shipper:
        if request.method == 'POST':
            form = AccountForm(request.POST)
            if form.is_valid():
                account = form.save(commit=False)
                account.user = request.user
                account.save()
                return redirect('dashboard')
        else:
            form = AccountForm()
        context = {
            'form': form
        }
        return render(request, 'create_account.html', context)
    elif request.user.is_merchant:
        if request.method == 'POST':
            form = AccountForm(request.POST)
            if form.is_valid():
                account = form.save(commit=False)
                account.user = request.user
                account.save()
                return redirect('dashboard')
        else:
            form = AccountForm()
        context = {
            'form': form
        }
        return render(request, 'create_account.html', context)

    else:
        return HttpResponse('You do not have access to this page')


@login_required()
def edit_account(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()
            return redirect('account_details')
    else:
        form = AccountForm(instance=account)
    context = {
        'form': form
    }
    return render(request, 'edit_account.html', context)


def account_details(request):
    if request.user.is_shipper is True:
        accounts = Account.objects.filter(user=request.user).select_related('user')
        context = {
            'accounts': accounts
        }
        return render(request, 'account_details.html', context)
    elif request.user.is_merchant is True:
        accounts = Account.objects.filter(user=request.user).select_related('user')
        context = {
            'accounts': accounts
        }
        return render(request, 'account_details.html', context)

    else:
        return HttpResponse('You do not have access to this page')


def make_payment(request, pk):
    order = get_object_or_404(Order, pk=pk)
    amount = order.final_price()
    response = Transaction.initialize(amount=amount, email=request.user.email,
                                      callback_url='http://localhost:8000/payment/my_payment/')
    url = response['data']['authorization_url']
    reference = response['data']['reference']
    payment = Payment.objects.create(user=request.user, reference=reference, amount=amount, order=order)
    payment.save()
    return redirect(url)


def payment_page(request):
    orders = OrderItem.objects.filter(product__merchant=request.user, ordered=True).select_related('user').\
                                     order_by('-date_created')
    context = {
        'orders': orders
    }
    return render(request, 'payment_verification.html', context)


def my_payment(request):
    order = Order.objects.get(user=request.user, is_ordered=False)
    payment = Payment.objects.get(order=order)
    response = Transaction.verify(reference=payment.reference)
    payment.user = request.user
    payment.amount = response['data']['amount']
    payment.status = response['data']['status']
    payment.channel = response['data']['channel']
    payment.card_type = response['data']['authorization']['card_type']
    payment.bank_name = response['data']['authorization']['bank']
    payment.save()
    payments = Payment.objects.filter(user=request.user).order_by('-payment_date').select_related('user', 'order')
    context = {
        'payments': payments
    }
    return render(request, 'payment_verification.html', context)