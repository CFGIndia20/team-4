from django.contrib import admin
from .models import Complaint, Category
# Register your models here.

admin.site.register(Complaint)
admin.site.register(Category)
