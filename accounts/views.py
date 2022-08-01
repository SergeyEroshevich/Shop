from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login

from .forms import LoginForm, RegistrationForm, ChangeUserlnfoForm
from .models import Profile

def registration(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User(**form.cleaned_data)
            user.set_password(request.POST['password'])
            user.save()
            profile = Profile(user=user)
            profile.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/registration.html', context)

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

# страница профиля
@login_required()
def profile(request):
    user = request.user
    profile, status = Profile.objects.get_or_create(user=user)
    context = {'user': user, 'p': profile}
    return render(request, 'accounts/profile.html', context)

@login_required()
def profile_change(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    form = ChangeUserlnfoForm(initial={'first_name':user.first_name,
                                       'last_name':user.last_name,
                                       'email':user.email,
                                       'postal_code':profile.postal_code,
                                       'city':profile.city,
                                       'street':profile.street,
                                       'house':profile.house,
                                       'building':profile.building,
                                       'apartment':profile.apartment,
                                       'phone':profile.phone}
                              )
    if request.method == 'POST':
        form = ChangeUserlnfoForm(request.POST)
        if form.is_valid():
            postal_code = form.cleaned_data.pop('postal_code')
            city = form.cleaned_data.pop('city')
            street = form.cleaned_data.pop('street')
            house = form.cleaned_data.pop('house')
            building = form.cleaned_data.pop('building')
            apartment = form.cleaned_data.pop('apartment')
            phone = form.cleaned_data.pop('phone')
            profile.postal_code = postal_code
            profile.city = city
            profile.street = street
            profile.house = house
            profile.building = building
            profile.apartment = apartment
            profile.phone = phone
            profile.save()
            user.first_name = form.cleaned_data.pop('first_name')
            user.last_name = form.cleaned_data.pop('last_name')
            user.email = form.cleaned_data.pop('email')
            user.save()
            return redirect('/accounts/profile/')
    context = {'form': form}
    return render(request, 'accounts/profile_change.html', context)

