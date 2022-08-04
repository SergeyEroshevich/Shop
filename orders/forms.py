from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['payment', 'delivery','postal_code', 'city', 'street', 'house', 'building', 'apartment']
