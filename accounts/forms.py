from django import forms
from django.contrib.auth.models import User

def validator_phone(value):
    if not value.isnumeric():
        raise forms.ValidationError('Поле должно содержать только цифры')
    if len(value) < 7:
        raise forms.ValidationError('Не хватает цифр')

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=30, label='Логин')
    password = forms.CharField(max_length=30, label='Пароль', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=30, label='Логин')
    first_name = forms.CharField(max_length=30, label='Имя')
    last_name = forms.CharField(max_length=30, label='Фамилия')
    password = forms.CharField(max_length=30, label='Пароль', widget=forms.PasswordInput())
    email = forms.EmailField(label='Электронная почта')
    # phone = forms.CharField(label='Телефон', validators = [validator_phone])
    # adress = forms.CharField(max_length=100, label='Адрес', widget=forms.Textarea)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')