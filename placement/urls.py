from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('about/', views.About, name='about'),
    path('allcompanies/', views.AllCompanies, name='allcompanies'),
    path('registeredcompanies/', views.RegisteredCompanies, name='registeredcompanies'),
    path('profile/', views.Profile, name='profile'),
    path('register/', views.RegisterDeregister, name='register-deregister'),
    path('edit-profile/', views.EditProfile, name='edit-profile'),
]