from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from .models import Product, Category
from authentication.models import CustomUser
from market.models import Market
from order.models import OrderItem
from django.contrib import messages
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .task import product_viewed, new_product_added


def home_view(request):
    markets = Market.objects.all()
    shops = CustomUser.objects.filter(is_merchant=True)[:5]
    context = {
        'markets': markets,
        'shops': shops
    }
    return render(request, 'market.html', context)


def search_view(request):
    search_product = request.GET.get('search')
    if search_product is not None:
        qs = Product.objects.filter(Q(title__contains=search_product) | Q(name__exact=search_product))
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
    all_products = Product.objects.filter(merchant=request.user).select_related('merchant', 'category', 'market' )
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
def my_product_list(request):
    categories = Category.objects.all()
    markets = Market.objects.all()
    if request.user.is_merchant is True:
        products = Product.objects.filter(merchant=request.user).order_by('id').select_related('merchant', 'category',
                                                                                               'market')
        paginator = Paginator(products, 10)
        page_number = request.GET.get('page')
        products = paginator.get_page(page_number)
        context = {
            'products': products,
            'categories': categories,
            'markets': markets
        }
        return render(request, 'my_product_list.html', context)
    else:
        raise PermissionDenied


@login_required
def my_product_grid(request):
    categories = Category.objects.all()
    markets = Market.objects.all()
    if request.user.is_merchant is True:
        products = Product.objects.filter(merchant=request.user).order_by('id').select_related('merchant', 'category',
                                                                                                 'market')
        paginator = Paginator(products, 10)
        page_number = request.GET.get('page')
        products = paginator.get_page(page_number)
        context = {
            'products': products,
            'categories': categories,
            'markets': markets
        }
        return render(request, 'my_product_grid.html', context)
    else:
        raise PermissionDenied


@login_required
def add_product(request):
    categories = Category.objects.all()
    markets = Market.objects.all()
    if request.user.is_merchant or request.user.is_admin and request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.merchant = request.user
            product.save()
            new_product_added.delay(product.pk)
            return redirect('my_product_grid')

        else:
            form = ProductForm(request.POST, request.FILES)
        context = {
            'categories': categories,
            'form': form,
            'markets': markets
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
    if request.user.is_merchant is True and product.merchant == request.user:
        product.delete()
        return redirect('my_product_grid')
    else:
        raise PermissionDenied


def detail_view(request, pk):
    detail = get_object_or_404(Product, pk=pk)
    detail.view_product += 1
    detail.save()
    product_viewed.delay(detail.pk)
    related_products = Product.objects.filter(category=detail.category).select_related('merchant',  'category',
                                                                                       'market')[:4]
    context = {
        'detail': detail,
        'related_product': related_products
    }
    return render(request, 'detail.html', context)


def view_category(request, category_name, market_name):
    category = Category.objects.get(name=category_name)
    market = Market.objects.get(name=market_name)
    products = Product.objects.filter(category=category, market=market).order_by('name').select_related('merchant',
                                                                                                        'category',
                                                                                                        'market')
    if products.exists():
        paginator = Paginator(products, 10)
        page_number = request.GET.get('page')
        products = paginator.get_page(page_number)
        context = {
            'products': products,
            'category': category
        }
        return render(request, 'categories.html', context)
    else:
        return render(request, '404.html')


def laptops_list(request):
    qs = Product.objects.filter(name='Laptop').order_by('id').select_related('merchant',)
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


def t_shirts_view(request):
    qs = Product.objects.filter(name='T-Shirts').order_by('id').select_related('merchant',)
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


def jeans_view(request):
    qs = Product.objects.filter(name='Jeans').order_by('id').select_related('merchant',)
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


def shirts_view(request):
    qs = Product.objects.filter(name='Shirts').order_by('id').select_related('merchant',)
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
    qs = Product.objects.filter(name='Watch').order_by('id').select_related('merchant', )
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


def home_theatre_view(request):
    qs = Product.objects.filter(name='Home Theatre').order_by('id').select_related('merchant',)
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
    qs = Product.objects.filter(name='Washing Machine').order_by('id').select_related('merchant',)
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


def sofa_view(request):
    qs = Product.objects.filter(name='Sofa').order_by('id').select_related('merchant',)
    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
                   'filter': qs
                  }
        return render(request, 'sofa_list.html', context)
    else:
        return render(request, '404.html')


def dining_set_view(request):
    qs = Product.objects.filter(name='Dining Set').order_by('id').select_related('merchant',)
    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
                   'filter': qs
                  }
        return render(request, 'dining_list.html', context)
    else:
        return render(request, '404.html')


def fans_view(request):
    qs = Product.objects.filter(name='Fan').order_by('id').select_related('merchant',)
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


def cement_view(request):
    qs = Product.objects.filter(name='Cement').order_by('id').select_related('merchant',)
    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
                   'filter': qs
                  }
        return render(request, 'cement_list.html', context)
    else:
        return render(request, '404.html')


def sand_view(request):
    qs = Product.objects.filter(name='Sand').order_by('id').select_related('merchant',)
    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
                   'filter': qs
                  }
        return render(request, 'sand_list.html', context)
    else:
        return render(request, '404.html')


def iron_rod_view(request):
    qs = Product.objects.filter(name='Iron Rod').order_by('id').select_related('merchant',)
    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
                   'filter': qs
                  }
        return render(request, 'iron_rod_list.html', context)
    else:
        return render(request, '404.html')


def wig_view(request):
    qs = Product.objects.filter(name='Wig').order_by('id').select_related('merchant',)
    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
                   'filter': qs
                  }
        return render(request, 'wig_list.html', context)
    else:
        return render(request, '404.html')


def lingerie_view(request):
    qs = Product.objects.filter(name='Lingerie').order_by('id').select_related('merchant',)
    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
                   'filter': qs
                  }
        return render(request, 'lingerie_list.html', context)
    else:
        return render(request, '404.html')


def body_cream_view(request):
    qs = Product.objects.filter(name='Body Cream').order_by('id').select_related('merchant',)
    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
                   'filter': qs
                  }
        return render(request, 'body_cream_list.html', context)
    else:
        return render(request, '404.html')


def grain_view(request):
    qs = Product.objects.filter(name='Grain').order_by('id').select_related('merchant',)
    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
                   'filter': qs
                  }
        return render(request, 'grain_list.html', context)
    else:
        return render(request, '404.html')


def tuber_view(request):
    qs = Product.objects.filter(name='Tuber').order_by('id').select_related('merchant',)
    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
                   'filter': qs
                  }
        return render(request, 'tuber_list.html', context)
    else:
        return render(request, '404.html')


def grocery_view(request):
    qs = Product.objects.filter(name='Grocery').order_by('id').select_related('merchant',)
    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
                   'filter': qs
                  }
        return render(request, 'grocery_list.html', context)
    else:
        return render(request, '404.html')


def vegetable_view(request):
    qs = Product.objects.filter(name='Vegetable').order_by('id').select_related('merchant',)
    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
                   'filter': qs
                  }
        return render(request, 'vegetable_list.html', context)
    else:
        return render(request, '404.html')


def frozen_view(request):
    qs = Product.objects.filter(name='Frozen Food').order_by('id').select_related('merchant',)
    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
                   'filter': qs
                  }
        return render(request, 'frozen_list.html', context)
    else:
        return render(request, '404.html')


def poultry_view(request):
    qs = Product.objects.filter(name='Poultry').order_by('id').select_related('merchant',)
    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
                   'filter': qs
                  }
        return render(request, 'poultry_list.html', context)
    else:
        return render(request, '404.html')


def livestock_view(request):
    qs = Product.objects.filter(name='Livestock').order_by('id').select_related('merchant',)
    if qs.exists():
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        qs = paginator.get_page(page_number)
        context = {
                   'filter': qs
                  }
        return render(request, 'livestock_list.html', context)
    else:
        return render(request, '404.html')