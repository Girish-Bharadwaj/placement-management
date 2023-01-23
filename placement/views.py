from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Profile as profile, Other_Details as other_details
from django.contrib.auth.models import User
from placement.models import Company as company, registered_companies, placed_students
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
    companies_data = company.objects.all()
    return render(request, 'placement/AllCompanies.html', {'companies': companies_data})


@login_required
def RegisteredCompanies(request):
    registered_companies_data = registered_companies.objects.filter(
        student=request.user)
    companies_data = []
    for registered_company in registered_companies_data:
        companies_data.append(registered_company.company)
    # get all profiles from job profile for all companies
    return render(request, 'placement/RegisteredCompanies.html', {'companies': companies_data})


@login_required
def Dashboard(request):
    # if student is placed from placed students
    # isPlaced = False
    # if placed_students.objects.filter(student=request.user).exists():
    #     isPlaced = True

    # return render(request, 'placement/Dashboard.html', {'isPlaced': isPlaced, 'company_name': placed_students.objects.filter(student=request.user).first().company.name})
    return render(request, 'placement/Dashboard.html')

@login_required
def RegisterDeregister(request):
    all_companies = company.objects.all()
    registered_companies_data = registered_companies.objects.filter(
        student=request.user).all()

    if request.method == 'POST':
        if 'register' in request.POST:
            selected_value = request.POST.get('register_company')
            selected_company = company.objects.filter(
                name=selected_value).first()
            # check if already registered
            if registered_companies.objects.filter(company=selected_company, student=request.user).exists():
                # deregister
                print("deregister")
            else:
                registered_companies.objects.create(
                    company=selected_company, student=request.user)
        else:
            selected_value = request.POST.get('deregister_company')
            selected_company = company.objects.filter(
                name=selected_value).first()
            registered_companies.objects.filter(
                company=selected_company, student=request.user).delete()

    return render(request, 'placement/Register-Deregister.html', {'all_companies': all_companies, 'registered_companies': registered_companies_data})


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
