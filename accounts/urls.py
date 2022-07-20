from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.to_profile, name='login'),
    path('logout/', views.profile_logout, name='logout'),
]