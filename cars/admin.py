from django.contrib import admin
from .models import Car, Feature, Category


# Register your models here.
admin.site.register(Car)
admin.site.register(Category)
admin.site.register(Feature)
