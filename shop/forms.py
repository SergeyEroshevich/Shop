from django import forms

from .models import Rating, Product, Category


class RatingForm(forms.ModelForm):
    CHOICES = ((1,1), (2,2), (3,3), (4,4), (5,5))
    rating = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label='Оценка')
    review = forms.CharField(widget=forms.Textarea, label='Отзыв', required=False)

    class Meta:
        model = Rating
        fields = ('rating', 'review')


class DiscountDeleteForm(forms.Form):
    product_discount = forms.ModelMultipleChoiceField(queryset=Product.objects.filter(discount=True),
                                                      widget=forms.CheckboxSelectMultiple,
                                                      label='Убрать скидку с товара',
                                                      required=False)

class DiscountForm(forms.Form):
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),
                                              widget=forms.CheckboxSelectMultiple,
                                              label='Выбрать всю категорию для скидки',
                                              required=False)

    product = forms.ModelMultipleChoiceField(queryset=Product.objects.filter(discount=False),
                                             label='Выбрать конкретный товар для скидки',
                                             required=False)

    discount = forms.IntegerField(min_value=0, max_value=100, label='Размер скидки')