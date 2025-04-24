from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Drink

admin.site.register(Drink)

class DrinkAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}