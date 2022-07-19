from django import forms

from .models import Brand


class SortForm(forms.Form):
    CHOICES = ((1, 'по убыванию цены'), (2, 'по возрастанию цены'), (3, 'по популярности'), (4, 'по рейтингу'), (5, 'новые'))
    sort = forms.ChoiceField(choices=CHOICES, label='Сортировать')


class SearchForm(forms.Form):
    discount = forms.BooleanField(label='Товары со скидкой', required=False)
    brand = forms.ModelMultipleChoiceField(queryset=Brand.objects.all(), widget=forms.CheckboxSelectMultiple, label='Производитель')
    price_from = forms.IntegerField(min_value=0, label='стоимость от', required=False)
    price_to = forms.IntegerField(min_value=0, label='стоимость до', required=False)