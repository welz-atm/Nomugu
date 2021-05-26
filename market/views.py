from django.shortcuts import render
from .models import Market


def is_valid_queryparam(param):
    return param is not None


def market_category(request, pk):
    market = Market.objects.get(pk=pk)
    context = {
            'market': market
        }
    return render(request, 'market_categories.html', context)


def market_laptops_list(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Laptop', market=market).order_by('id').select_related('merchant', 'category',
                                                                                            'market')
    brand = request.GET.get('brand')
    processor = request.GET.get('processor')
    ram = request.GET.get('ram')
    hdd = request.GET.get('hdd')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(title__contains=brand)

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(processor) and processor != 'Choose...':
        qs = qs.filter(title__contains=processor)

    if is_valid_queryparam(ram) and ram != 'Choose...':
        qs = qs.filter(title__contains=ram)

    if is_valid_queryparam(series) and hdd != 'Choose...':
        qs = qs.filter(title__contains=hdd)

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


def market_servers_list(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Server', market=market).order_by('id').select_related('merchant', 'category',
                                                                                            'market')
    brand = request.GET.get('brand')
    processor = request.GET.get('processor')
    ram = request.GET.get('ram')
    series = request.GET.get('series')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(title__contains=brand)

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(processor) and processor != 'Choose...':
        qs = qs.filter(title__contains=processor)

    if is_valid_queryparam(ram) and ram != 'Choose...':
        qs = qs.filter(title__contains=ram)

    if is_valid_queryparam(series) and series != 'Choose...':
        qs = qs.filter(title__contains=series)

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


def market_desktops_list(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Desktop', market=market).order_by('id').select_related('merchant', 'category',
                                                                                             'market')
    brand = request.GET.get('brand')
    processor = request.GET.get('processor')
    ram = request.GET.get('ram')
    series = request.GET.get('series')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(title__contains=brand)

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(processor) and processor != 'Choose...':
        qs = qs.filter(title__contains=processor)

    if is_valid_queryparam(ram) and ram != 'Choose...':
        qs = qs.filter(title__contains=ram)

    if is_valid_queryparam(series) and series != 'Choose...':
        qs = qs.filter(title__contains=series)

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


def market_network_list(request):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Desktop', market=market).order_by('id').select_related('merchant',)
    brand = request.GET.get('brand')
    type = request.GET.get('type')
    series = request.GET.get('series')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(title__contains=brand)

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(type) and type != 'Choose...':
        qs = qs.filter(title__contains=type)

    if is_valid_queryparam(series) and series != 'Choose...':
        qs = qs.filter(title__contains=series)

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


def market_android_list(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Android', market=market).order_by('id').select_related('merchant',)
    brand = request.GET.get('brand')
    ram = request.GET.get('ram')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(title__contains=brand)

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(ram) and ram != 'Choose...':
        qs = qs.filter(title__contains=ram)

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


def market_ios_list(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='IOS', market=market).order_by('id').select_related('merchant',)
    brand = request.GET.get('brand')
    proc = request.GET.get('proc')
    ram = request.GET.get('ram')
    series = request.GET.get('series')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(title__contains=brand)

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(proc) and proc != 'Choose...':
        qs = qs.filter(title__contains=proc)

    if is_valid_queryparam(ram) and ram != 'Choose...':
        qs = qs.filter(title__contains=ram)

    if is_valid_queryparam(series) and series != 'Choose...':
        qs = qs.filter(title__contains=series)

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


def market_clothing_view(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Clothing', market=market).order_by('id').select_related('merchant',)
    brand = request.GET.get('brand')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    color = request.GET.get('color')
    size = request.GET.get('size')
    type = request.GET.get('type')

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(brand__exact=brand)

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(color) and color != 'Choose...':
        qs = qs.filter(color__exact=color)

    if is_valid_queryparam(size) and size != 'Choose...':
        qs = qs.filter(title__contains=size)

    if is_valid_queryparam(type) and type != 'Choose...':
        qs = qs.filter(title__contains=type)

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


def market_footwear_view(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Footwear', market=market).order_by('id').select_related('merchant',)
    brand = request.GET.get('brand')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    color = request.GET.get('color')
    size = request.GET.get('size')
    type = request.GET.get('type')

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(brand__exact=brand)

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(color) and color != 'Choose...':
        qs = qs.filter(color__exact=color)

    if is_valid_queryparam(size) and size != 'Choose...':
        qs = qs.filter(title__contains=size)

    if is_valid_queryparam(type) and type != 'Choose...':
        qs = qs.filter(title__contains=type)

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


def market_fragrance_view(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Fragrance', market=market).order_by('id').select_related('merchant',)
    brand = request.GET.get('brand')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    color = request.GET.get('color')
    size = request.GET.get('size')
    type = request.GET.get('type')

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(brand__exact=brand)

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(color) and color != 'Choose...':
        qs = qs.filter(color__exact=color)

    if is_valid_queryparam(size) and size != 'Choose...':
        qs = qs.filter(title__contains=size)

    if is_valid_queryparam(type) and type != 'Choose...':
        qs = qs.filter(title__contains=type)

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'fragrance_list.html', context)
    else:
        return render(request, '404.html')


def market_watch_view(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Watch', market=market).order_by('id').select_related('merchant', )
    brand = request.GET.get('brand')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    color = request.GET.get('color')
    type = request.GET.get('type')

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(brand__exact=brand)

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(color) and color != 'Choose...':
        qs = qs.filter(color__exact=color)

    if is_valid_queryparam(type) and type != 'Choose...':
        qs = qs.filter(title__contains=type)

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


def market_fabrics_view(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Fabrics', market=market).order_by('id').select_related('merchant',)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    color = request.GET.get('color')
    country = request.GET.get('country')
    sex = request.GET.get('sex')
    type = request.GET.get('type')

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(color) and color != 'Choose...':
        qs = qs.filter(color__exact=color)

    if is_valid_queryparam(country) and country != 'Choose...':
        qs = qs.filter(title__contains=country)

    if is_valid_queryparam(sex) and sex != 'Choose...':
        qs = qs.filter(sex__exact=sex)

    if is_valid_queryparam(type) and type != 'Choose...':
        qs = qs.filter(title__contains=type)

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


def market_tv_view(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Television', market=market).order_by('id').select_related('merchant',)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    brand = request.GET.get('brand')
    type = request.GET.get('type')

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(brand__exact=brand)

    if is_valid_queryparam(type) and type != 'Choose...':
        qs = qs.filter(title__contains=type)

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'tv_list.html', context)
    else:
        return render(request, '404.html')


def market_ac_view(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Air Conditioner', market=market).order_by('id').select_related('merchant',)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    brand = request.GET.get('brand')
    horsepower = request.GET.get('hp')
    type = request.GET.get('type')

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(brand__exact=brand)

    if is_valid_queryparam(horsepower) and horsepower != 'Choose...':
        qs = qs.filter(title__contains=horsepower)

    if is_valid_queryparam(type) and type != 'Choose...':
        qs = qs.filter(title__contains=type)

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'ac_list.html', context)
    else:
        return render(request, '404.html')


def market_audio_view(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Audio', market=market).order_by('id').select_related('merchant',)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    brand = request.GET.get('brand')
    type = request.GET.get('type')

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(brand__exact=brand)

    if is_valid_queryparam(type) and type != 'Choose...':
        qs = qs.filter(title__contains=type)

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'audio_list.html', context)
    else:
        return render(request, '404.html')


def market_refrigerator_view(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Refrigerator', market=market).order_by('id').select_related('merchant',)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    brand = request.GET.get('brand')
    type = request.GET.get('type')
    color = request.GET.get('color')

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(brand__exact=brand)

    if is_valid_queryparam(color) and color != 'Choose...':
        qs = qs.filter(color__exact=color)

    if is_valid_queryparam(type) and type != 'Choose...':
        qs = qs.filter(title__contains=type)

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'refrigerator_list.html', context)
    else:
        return render(request, '404.html')


def market_freezer_view(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Freezer', market=market).order_by('id').select_related('merchant',)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    brand = request.GET.get('brand')
    type = request.GET.get('type')
    color = request.GET.get('color')

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(brand__exact=brand)

    if is_valid_queryparam(color) and color != 'Choose...':
        qs = qs.filter(title__contains=color)

    if is_valid_queryparam(type) and type != 'Choose...':
        qs = qs.filter(title__contains=type)

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'freezer_list.html', context)
    else:
        return render(request, '404.html')


def market_cookers_view(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Cooker', market=market).order_by('id').select_related('merchant',)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    brand = request.GET.get('brand')
    type = request.GET.get('type')

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(brand__exact=brand)

    if is_valid_queryparam(type) and type != 'Choose...':
        qs = qs.filter(title__contains=type)

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'cookers_list.html', context)
    else:
        return render(request, '404.html')


def market_microwave_view(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Microwave', market=market).order_by('id').select_related('merchant',)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    brand = request.GET.get('brand')
    type = request.GET.get('type')

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(brand__exact=brand)

    if is_valid_queryparam(type) and type != 'Choose...':
        qs = qs.filter(title__contains=type)

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'microwave_list.html', context)
    else:
        return render(request, '404.html')


def market_dispenser_view(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Dispenser', market=market).order_by('id').select_related('merchant',)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    brand = request.GET.get('brand')

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(brand__exact=brand)

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'dispenser_list.html', context)
    else:
        return render(request, '404.html')


def market_blender_view(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Blender', market=market).order_by('id').select_related('merchant',)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    brand = request.GET.get('brand')

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(brand__exact=brand)

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'blender_list.html', context)
    else:
        return render(request, '404.html')


def market_kettle_view(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Kettle', market=market).order_by('id').select_related('merchant',)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    brand = request.GET.get('brand')
    type = request.GET.get('type')

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(brand__exact=brand)

    if is_valid_queryparam(type) and type != 'Choose...':
        qs = qs.filter(title__contains=type)

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'kettles_list.html', context)
    else:
        return render(request, '404.html')


def market_washers_view(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Washers', market=market).order_by('id').select_related('merchant',)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    brand = request.GET.get('brand')
    type = request.GET.get('type')
    color = request.GET.get('color')

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(brand__exact=brand)

    if is_valid_queryparam(color) and color != 'Choose...':
        qs = qs.filter(title__contains=color)

    if is_valid_queryparam(type) and type != 'Choose...':
        qs = qs.filter(title__contains=type)

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'washers_list.html', context)
    else:
        return render(request, '404.html')


def market_furniture_view(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Furniture', market=market).order_by('id').select_related('merchant',)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    brand = request.GET.get('brand')
    type = request.GET.get('type')

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(brand__exact=brand)

    if is_valid_queryparam(type) and type != 'Choose...':
        qs = qs.filter(title__contains=type)

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'furniture_list.html', context)
    else:
        return render(request, '404.html')


def market_fans_view(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Fans', market=market).order_by('id').select_related('merchant',)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    brand = request.GET.get('brand')
    type = request.GET.get('type')
    charge = request.GET.get('charge')

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(brand__exact=brand)

    if is_valid_queryparam(charge) and charge != 'Choose...':
        qs = qs.filter(color__exact=charge)

    if is_valid_queryparam(type) and type != 'Choose...':
        qs = qs.filter(title__contains=type)

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'fans_list.html', context)
    else:
        return render(request, '404.html')


def market_bed_view(request, pk):
    market = get_object_or_404(Market, pk=pk)
    qs = Product.objects.filter(name='Bed', market=market).order_by('id').select_related('merchant',)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    brand = request.GET.get('brand')
    type = request.GET.get('type')
    size = request.GET.get('size')

    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)

    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lte=max_price)

    if is_valid_queryparam(brand) and brand != 'Choose...':
        qs = qs.filter(brand__exact=brand)

    if is_valid_queryparam(type) and type != 'Choose...':
        qs = qs.filter(title__contains=type)

    if is_valid_queryparam(size) and size != 'Choose...':
        qs = qs.filter(title__contains=size)

    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
            'filter': qs,
            'market': market,
        }
        return render(request, 'bed_list.html', context)
    else:
        return render(request, '404.html')
