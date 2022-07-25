from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login

from .forms import LoginForm, RegistrationForm


# вход в аккаунт
def to_profile(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/login.html', context)

# выход из аккаунта
def profile_logout(request):
    logout(request)
    return redirect('/')

@login_required()
def profile(request):
    return render(request, 'accounts/profile.html')

def registration(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User(**form.cleaned_data)
            user.set_password(request.POST['password'])
            user.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/registration.html', context)