from django import forms

from .models import Brand


class SortForm(forms.Form):
    CHOICES = ((1, 'по убыванию цены'), (2, 'по возрастанию цены'), (3, 'новые'))
    sort = forms.ChoiceField(choices=CHOICES, label='Сортировать')

