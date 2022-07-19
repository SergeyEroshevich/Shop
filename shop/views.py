from django.shortcuts import render, get_object_or_404

from .forms import SortForm, SearchForm
from .models import Category, Product, Image
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    form_sort = SortForm()
    form_search = SearchForm()
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {'category': category, 'categories': categories, 'products': products, 'form_sort': form_sort, 'form_search': form_search}
    return render(request, 'shop/product/list.html', context)



def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    img = Image.objects.filter(product_id=id)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form, 'img': img})

def pro(request):
    return render(request, 'index.html')
