from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<category_slug>/', views.product_list, name='product_list_by_category'),
    path('<id>/<slug>/', views.product_detail, name='product_detail'),
    path('shipping', views.shipping, name='shipping'),
    path('contacts', views.contacts, name='contacts'),
    path('payment', views.payment, name='payment'),
    path('discounts', views.discounts, name='discounts'),
    path('1/', views.pro),
]