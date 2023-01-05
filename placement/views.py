from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def Home(request):
    return render(request, 'placement/home.html',{
        'posts':["hello", "world", "test"]
    })

@login_required
def About(request):
    return render(request, 'placement/about.html')

@login_required
def Profile(request):
    return render(request, 'placement/profile.html')

@login_required
def AllCompanies(request):
    return render(request, 'placement/AllCompanies.html')

@login_required
def RegisteredCompanies(request):
    return render(request, 'placement/RegisteredCompanies.html')

@login_required
def Dashboard(request):
    return render(request, 'placement/Dashboard.html')

@login_required
def RegisterDeregister(request):
    return render(request, 'placement/Register-Deregister.html')

@login_required
def EditProfile(request):
    return render(request, 'placement/EditProfile.html')