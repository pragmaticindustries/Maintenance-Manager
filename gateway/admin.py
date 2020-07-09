from django.contrib import admin
from .models import Machine, Company


# Register your models here.
admin.site.register(Company)
admin.site.register(Machine)