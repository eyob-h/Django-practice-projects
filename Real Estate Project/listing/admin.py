from django.contrib import admin
# Register your models here.

from . import models

class ListingAdmin(admin.ModelAdmin):
    # fields = ['title','price']
    # list_diplay = ["title", "price", "address"]  YOU MISSPELLED DISPLAY!
    list_display = ["title", "price", "address", "date_listed"]

admin.site.register(models.Listing, ListingAdmin)
admin.site.register(models.Status)