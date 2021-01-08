from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from .models import Product, Category
from order.models import OrderItem
from django.contrib import messages
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def home_view(request):
    return render(request, 'home.html', {})


def search_view(request):
    qs = Product.objects.all()
    search_product = request.GET.get('search')
    if search_product is not None:
        qs = qs.filter((Q(title__contains=search_product) | Q(name__exact=search_product) | Q(category=search_product)))
        if qs.exists():
            paginator = Paginator(qs, 10)
            page_number = request.GET.get('page')
            qs = paginator.get_page(page_number)
            context = {
                   'qs': qs
                  }
            return render(request, 'search.html', context)
        else:
            return render(request, '404.html')


@login_required
def dashboard(request):
    all_products = Product.objects.filter(merchant=request.user).select_related('merchant', )
    products = all_products.count()
    orders = OrderItem.objects.filter(ordered=True).count()
    delivered = OrderItem.objects.filter(delivered=True).count()
    context = {
        'products': products,
        'delivered': delivered,
        'orders': orders,
        'all_products': all_products
      }
    return render(request, 'dashboard.html', context)


@login_required
def my_product(request):
    if request.user.is_merchant is True:
        products = Product.objects.filter(merchant=request.user)
        paginator = Paginator(products, 10)
        page_number = request.GET.get('page')
        products = paginator.get_page(page_number)
        context = {
            'products': products
        }
        return render(request, 'my_product.html', context)
    else:
        raise PermissionDenied


@login_required
def add_product(request):
    categories = Category.objects.all()
    if request.user.is_merchant is True:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.merchant = request.user
                product.save()
                messages.success(request, 'Product added successfully')
                return redirect('my_product')

        else:
            form = ProductForm(request.POST, request.FILES)

        context = {
            'categories': categories,
            'form': form,
            }

        return render(request, 'add_product.html', context)
    elif request.user.is_admin is True:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.merchant = request.user
                product.save()
                messages.success(request, 'Product added successfully')
                return redirect('my_product')

        else:
            form = ProductForm(request.POST, request.FILES)

        context = {
            'categories': categories,
            'form': form,
            }

        return render(request, 'add_product.html', context)
    else:
        raise PermissionDenied


@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    categories = Category.objects.all()
    if request.user.is_merchant is True and product.merchant == request.user:
        if request.method == 'POST':
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                prod = form.save(commit=False)
                prod.user = request.user
                prod.save()
                messages.success(request, 'Update successful.')
                return redirect('my_product')

        else:
            form = ProductForm(instance=product)
        context = {
            'form': form,
            'product': product,
            'categories': categories
        }
        return render(request, 'edit_productform.html', context)
    else:
        raise PermissionDenied


@login_required
def delete_product(request,pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user.is_merchant is True:
        product.delete()
        return redirect('my_product')
    else:
        raise PermissionDenied


def detail_view(request, pk):
    detail = get_object_or_404(Product, pk=pk)
    detail.view_product += 1
    detail.save()
    context = {
        'detail': detail,
    }
    return render(request, 'detail.html', context)


def is_valid_queryparam(param):
    return param is not None


def laptops_list(request):
    qs = Product.objects.filter(name='Laptop').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'laptop_list.html', context)
    else:
        return render(request, '404.html')


def servers_list(request):
    qs = Product.objects.filter(name='Server').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'server_list.html', context)
    else:
        return render(request, '404.html')


def desktops_list(request):
    qs = Product.objects.filter(name='Desktop').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'desktop_list.html', context)
    else:
        return render(request, '404.html')


def network_list(request):
    qs = Product.objects.filter(name='Desktop').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'networking_list.html', context)
    else:
        return render(request, '404.html')


def android_list(request):
    qs = Product.objects.filter(name='Android').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'android_list.html', context)
    else:
        return render(request, '404.html')


def ios_list(request):
    qs = Product.objects.filter(name='IOS').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'ios_list.html', context)
    else:
        return render(request, '404.html')


def clothing_view(request):
    qs = Product.objects.filter(name='Clothing').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'clothing_list.html', context)
    else:
        return render(request, '404.html')


def footwear_view(request):
    qs = Product.objects.filter(name='Footwear').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'footwear_list.html', context)
    else:
        return render(request, '404.html')


def fragrance_view(request):
    qs = Product.objects.filter(name='Fragrance').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'fragrance_list.html', context)
    else:
        return render(request, '404.html')


def watch_view(request):
    qs= Product.objects.filter(name='Watch').order_by('id').select_related('merchant', )
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
                   'filter': qs
                  }
        return render(request, 'watches_list.html', context)
    else:
        return render(request, '404.html')


def fabrics_view(request):
    qs = Product.objects.filter(name='Fabric').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'fabrics_list.html', context)
    else:
        return render(request, '404.html')


def tv_view(request):
    qs = Product.objects.filter(name='Television').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'tv_list.html', context)
    else:
        return render(request, '404.html')


def ac_view(request):
    qs = Product.objects.filter(name='Air Conditioner').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'ac_list.html', context)
    else:
        return render(request, '404.html')


def audio_view(request):
    qs = Product.objects.filter(name='Audio').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'audio_list.html', context)
    else:
        return render(request, '404.html')


def refrigerator_view(request):
    qs = Product.objects.filter(name='Refrigerator').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'refrigerator_list.html', context)
    else:
        return render(request, '404.html')


def freezer_view(request):
    qs = Product.objects.filter(name='Freezer').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'freezer_list.html', context)
    else:
        return render(request, '404.html')


def cookers_view(request):
    qs = Product.objects.filter(name='Cooker').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'cookers_list.html', context)
    else:
        return render(request, '404.html')


def microwave_view(request):
    qs = Product.objects.filter(name='Microwave').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'microwave_list.html', context)
    else:
        return render(request, '404.html')


def dispenser_view(request):
    qs = Product.objects.filter(name='Dispenser').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'dispenser_list.html', context)
    else:
        return render(request, '404.html')


def blender_view(request):
    qs = Product.objects.filter(name='Blender').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'blender_list.html', context)
    else:
        return render(request, '404.html')


def kettle_view(request):
    qs = Product.objects.filter(name='Kettle').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'kettles_list.html', context)
    else:
        return render(request, '404.html')


def washers_view(request):
    qs = Product.objects.filter(name='Washers').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'washers_list.html', context)
    else:
        return render(request, '404.html')


def furniture_view(request):
    qs= Product.objects.filter(name='Furniture').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'furniture_list.html', context)
    else:
        return render(request, '404.html')


def fans_view(request):
    qs = Product.objects.filter(name='Fans').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'fans_list.html', context)
    else:
        return render(request, '404.html')


def bed_view(request):
    qs = Product.objects.filter(name='Bed').order_by('id').select_related('merchant',)
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
                   'filter': qs
                  }
        return render(request, 'bed_list.html', context)
    else:
        return render(request, '404.html')


