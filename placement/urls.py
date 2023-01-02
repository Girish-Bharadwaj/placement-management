from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('allcompanies/', views.AllCompanies, name='allcompanies'),
    path('registeredcompanies/', views.RegisteredCompanies, name='registeredcompanies'),
    path('profile/', views.Profile, name='profile'),
]