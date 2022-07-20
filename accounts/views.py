from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login

from .forms import LoginForm


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

def profile_logout(request):
    logout(request)
    return redirect('/')
