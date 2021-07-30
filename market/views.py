from django.shortcuts import render
from .models import Market


def market_category(request, market_name):
    market = Market.objects.get(name=market_name)
    context = {
            'market': market
        }
    return render(request, 'market_categories.html', context)


def market_grain_view(request, market_name):
    market = Market.objects.get(name=market_name)
    qs = Product.objects.filter(name='Laptop', market=market).order_by('id').select_related('merchant', 'category',
                                                                                            'market')

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'laptop_list.html', context)
    else:
        return render(request, '404.html')


def market_tuber_view(request, market_name):
    market = Market.objects.get(name=market_name)
    qs = Product.objects.filter(name='Server', market=market).order_by('id').select_related('merchant', 'category',
                                                                                            'market')

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'server_list.html', context)
    else:
        return render(request, '404.html')


def market_grocery_view(request, market_name):
    market = Market.objects.get(name=market_name)
    qs = Product.objects.filter(name='Desktop', market=market).order_by('id').select_related('merchant', 'category',
                                                                                             'market')

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'desktop_list.html', context)
    else:
        return render(request, '404.html')


def market_vegetable_view(request, market_name):
    market = Market.objects.get(name=market_name)
    qs = Product.objects.filter(name='Desktop', market=market).order_by('id').select_related('merchant',)

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'networking_list.html', context)
    else:
        return render(request, '404.html')


def market_frozen_view(request, market_name):
    market = Market.objects.get(name=market_name)
    qs = Product.objects.filter(name='Android', market=market).order_by('id').select_related('merchant',)

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'android_list.html', context)
    else:
        return render(request, '404.html')


def market_poultry_view(request, market_name):
    market = Market.objects.get(name=market_name)
    qs = Product.objects.filter(name='IOS', market=market).order_by('id').select_related('merchant',)

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'ios_list.html', context)
    else:
        return render(request, '404.html')


def market_livestock_view(request, market_name):
    market = Market.objects.get(name=market_name)
    qs = Product.objects.filter(name='Clothing', market=market).order_by('id').select_related('merchant',)

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'clothing_list.html', context)
    else:
        return render(request, '404.html')


def market_footwear_view(request, market_name):
    market = Market.objects.get(name=market_name)
    qs = Product.objects.filter(name='Footwear', market=market).order_by('id').select_related('merchant',)

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'footwear_list.html', context)
    else:
        return render(request, '404.html')


def market_watch_view(request, market_name):
    market = Market.objects.get(name=market_name)
    qs = Product.objects.filter(name='Watch', market=market).order_by('id').select_related('merchant', )

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'watches_list.html', context)
    else:
        return render(request, '404.html')


def market_fabrics_view(request, market_name):
    market = Market.objects.get(name=market_name)
    qs = Product.objects.filter(name='Fabrics', market=market).order_by('id').select_related('merchant',)
    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'fabrics_list.html', context)
    else:
        return render(request, '404.html')
