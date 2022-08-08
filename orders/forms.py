from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    building = forms.CharField(label='Корпус', widget=forms.TextInput(attrs={'placeholder': 'корпус'}))


    class Meta:
        model = Order
        fields = ['payment', 'delivery','postal_code', 'city', 'street', 'house', 'building', 'apartment']

    # def __init__(self, *args, **kwargs):
    #     super(OrderCreateForm, self).__init__(*args, **kwargs)
    #     for field in iter(self.fields):
    #         self.fields[field].widget.attrs.update({'class': 'form-control'})

    # def __init__(self, *args, **kwargs):
    #     super(OrderCreateForm, self).__init__(*args, **kwargs)
    #     self.fields['building'].widget.attrs.update({'placeholder': 'корпус'})