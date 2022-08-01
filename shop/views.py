from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .filter import ProductFilter
from .forms import RatingForm,  DiscountForm, DiscountDeleteForm
from .models import Category, Product, Image,  Rating
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# class ProductListView(ListView):
#     paginate_by = 3
#     model = Product
#     template_name = 'shop/product/list.html'


# список всех товаров на сайте
def product_list(request, category_slug=None, page=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    filter = ProductFilter(request.GET, queryset=products)
    paginator = Paginator(filter.qs, 6)
    if 'page' in request.GET:
        page_number = request.GET['page']
    else:
        page_number = 1
    page_obj = paginator.get_page(page_number)
    context = {'category': category, 'categories': categories, 'products': page_obj.object_list, 'page_obj': page_obj, 'paginator': paginator, 'filter': filter}
    return render(request, 'shop/product/list.html', context)


# детальная информация о товаре
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    rating = Rating.objects.filter(product=product)
    img = Image.objects.filter(product_id=id)
    cart_product_form = CartAddProductForm()
    count = int(str(rating.count())[-1])
    if count == 1:
        word = 'отзыв'
    elif 1 < count < 5:
        word = 'отзыва'
    else:
        word = 'отзывов'
    context = {'product': product, 'cart_product_form': cart_product_form, 'img': img, 'count': rating.count, 'word': word}
    return render(request, 'shop/product/detail.html', context)


def product_review(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {'product': product}
    return render(request, 'shop/product/review.html', context)


@login_required()
def review_and_rating(request, product_id):
    form = RatingForm()
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        # возможность изменять рейтинг товара вместо того чтобы иметь возможность оценивать только один раз
        # updated_values = {'rating': request.POST['rating']}
        # rating, created = Rating.objects.update_or_create(product=product, user=request.user, defaults=updated_values)
        rating = Rating.objects.create(product=product, user=request.user, rating=request.POST['rating'], review=request.POST.get('review'))
        rating.save()
        if product.rating == None:
            product.rating = request.POST['rating']
        else:
            count = product.product_rating.count()
            sum = 0
            for i in product.product_rating.all():
                sum += i.rating
            rating = sum/count
            product.rating = round(rating, 1)
        product.save()
        return redirect('/orders/my_orders/')
    context = {'product':product, 'form':form}
    return render(request, 'shop/product/add_review_and_rating.html', context)


@staff_member_required
def discount_managment(request):
    form = DiscountForm()
    form_delete = DiscountDeleteForm()
    products = Product.objects.filter(discount=True)
    if request.method == 'POST':
        if request.POST.get('product'):
            products_for_discount = request.POST.getlist('product')
            for product in products_for_discount:
                product = Product.objects.get(id=product)
                product.discount = True
                sale = 1 - int(request.POST.get('discount'))/100
                product.sale = sale
                product.save()
        if request.POST.get('category'):
            category_discount = request.POST.getlist('category')
            for category in category_discount:
                category = Category.objects.get(id=category)
                products = Product.objects.filter(category=category)
                for product in products:
                    product.discount = True
                    sale = 1 - int(request.POST.get('discount')) / 100
                    product.sale = sale
                    product.save()
        if request.POST.get('product_discount'):
            product_discount = request.POST.getlist('product_discount')
            for product in product_discount:
                product = Product.objects.get(id=product)
                product.discount = False
                product.sale = 1
                product.save()

    context = {'products':products, 'form': form, 'form_delete':form_delete}
    return render(request, 'shop/discount_managment/discount_managment.html', context)


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
