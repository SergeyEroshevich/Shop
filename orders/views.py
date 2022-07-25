from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart

@login_required()
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.buyer = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})

# все заказы с сайта для персонала
@login_required()
def  all_orders(request):
    # orders = Order.objects.filter(buyer=request.user).order_by('-created')
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'orders/all_orders.html', context)

# заказы покупателя
@login_required()
def  my_orders(request):
    orders = Order.objects.filter(buyer=request.user)
    context = {'orders': orders}
    return render(request, 'orders/my_orders.html', context)