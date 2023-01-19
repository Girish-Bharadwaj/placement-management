from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Profile as profile, Other_Details as other_details
from django.contrib.auth.models import User
from django import forms
# Create your views here.


def Home(request):
    return render(request, 'placement/home.html', {
        'posts': ["hello", "world", "test"]
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


class EditProfile(LoginRequiredMixin, UpdateView):
    model = other_details
    fields = ['address', 'dob', 'father_name', 'mother_name', 'category']
    template_name = 'placement/EditProfile.html'
    success_url = '/profile'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            self.object.address = form.cleaned_data['address']
            self.object.dob = form.cleaned_data['dob']
            self.object.father_name = form.cleaned_data['father_name']
            self.object.mother_name = form.cleaned_data['mother_name']
            self.object.category = form.cleaned_data['category']
            print(self.object)
            self.object.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_object(self, queryset=None):
        obj = other_details.objects.filter(id=profile.objects.filter(
            user=self.request.user).first().other_details.id).first()
        return obj
