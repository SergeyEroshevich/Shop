from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .filter import ProductFilter
from .forms import SortForm
from .models import Category, Product, Image
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# class ProductListView(ListView):
#     paginate_by = 3
#     model = Product
#     template_name = 'shop/product/list.html'

# список всех товаров на сайте
def product_list(request, category_slug=None, page=None):
    form_sort = SortForm()
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    filter = ProductFilter(request.GET, queryset=products)
    paginator = Paginator(filter.qs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {'category': category, 'categories': categories, 'products': products, 'form_sort': form_sort,
                        'page_obj': page_obj, 'paginator': paginator, 'filter': filter}
    return render(request, 'shop/product/list.html', context)

# детальная информация о товаре
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    img = Image.objects.filter(product_id=id)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form, 'img': img})


def shipping(request):
    return render(request, 'shop/information_shop/shipping.html')

def contacts(request):
    return render(request, 'shop/information_shop/contacts.html')

def discounts(request):
    return render(request, 'shop/information_shop/discounts.html')

def payment(request):
    return render(request, 'shop/information_shop/payment.html')

# мое резюме
def pro(request):
    return render(request, 'index.html')
