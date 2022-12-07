from django.contrib import admin

from .models import Company, Developers

# Register your models here.

admin.site.register(Developers)
admin.site.register(Company)