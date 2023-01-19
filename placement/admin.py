from django.contrib import admin
from .models import Company, job_profile, registered_companies, placed_students

# Register your models here.
admin.site.register(Company)
admin.site.register(job_profile)
admin.site.register(registered_companies)
admin.site.register(placed_students)
