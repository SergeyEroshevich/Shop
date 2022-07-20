from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=30, label='Логин')
    password = forms.CharField(max_length=30, label='Пароль', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')