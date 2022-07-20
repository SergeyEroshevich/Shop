from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .forms import SortForm, SearchForm
from .models import Category, Product, Image
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator


# class ProductListView(ListView):
#     paginate_by = 2
#     model = Product
#     template_name = 'shop/product/list.html'


def product_list(request, category_slug=None):
    form_sort = SortForm()
    form_search = SearchForm()
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    if request.method == 'POST':
        products = get_product_for_parameter(request.POST, products)

    paginator = Paginator(products, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'category': category, 'categories': categories, 'products': products, 'form_sort': form_sort,
                       'form_search': form_search, 'page_obj': page_obj, 'paginator': paginator}
    return render(request, 'shop/product/list.html', context)


def get_product_for_parameter(parameter , products):
    if parameter.get('discount') == 'on':
        products = products.filter(discount=True)
    if parameter.get('brand'):
        brands = parameter.getlist('brand')
        products = products.filter(brand__in=[i for i in brands])
    if parameter.get('price_from'):
        products = products.filter(res_sale__gte=parameter.get('price_from'))
    if parameter.get('price_to'):
        products = products.filter(res_sale__lte=parameter.get('price_to'))
    if parameter.get('sort'):
        atrr = int(parameter.get('sort'))
        method_sort = {1: '-price', 2: 'price', 3: '-res2', 4: '-rating', 5: 'created'}
        def sort(method, product):
            products = product.order_by(method)
            return products
        products = sort(method_sort.get(atrr), products)
    return products


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    img = Image.objects.filter(product_id=id)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form, 'img': img})

def pro(request):
    return render(request, 'index.html')
