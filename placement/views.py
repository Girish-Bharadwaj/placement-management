from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    return render(request, 'placement/home.html',{
        'posts':["hello", "world", "test"]
    })


def About(request):
    return render(request, 'placement/about.html')

def Profile(request):
    return render(request, 'placement/profile.html')

def AllCompanies(request):
    return render(request, 'placement/AllCompanies.html')

def RegisteredCompanies(request):
    return render(request, 'placement/RegisteredCompanies.html')