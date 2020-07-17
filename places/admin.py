from django.contrib import admin
from .models import Place, Image


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image)