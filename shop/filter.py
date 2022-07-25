from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from django_filters.widgets import LinkWidget
from rest_framework import generics
from django.db import models
from django import forms

from .models import Product, Brand


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Название')
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label='Цена от')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt', label='Цена до')
    brand = django_filters.ModelMultipleChoiceFilter(queryset=Brand.objects.all())

    ordering = django_filters.OrderingFilter(label='Упорядочить', choices=(('price', 'цена по возрастанию'),
                                                                              ('-price', 'цена по убыванию'),
                                                                              ('name', 'по названию'),
                                                                              ('-rating', 'по рейтингу'),
                                                                              ('-created', 'новые'),))
    class Meta:
        model = Product
        fields = ['name', 'discount', 'brand']
        filter_overrides = {
            models.BooleanField:{
                'filter_class': django_filters.BooleanFilter,
                'extra': lambda f: {
                    'widget': forms.CheckboxInput,
                },
            },
            # models.ForeignKey:{
            #     'filter_class': django_filters.ModelMultipleChoiceFilter,
            #     'extra': lambda f: {
            #         'widget': forms.CheckboxSelectMultiple,
            #     },
            # },
        }

# class UserListView(generics.ListAPIView):
#     filter_backends = [DjangoFilterBackend]