from django.contrib import admin

from .models import Image, Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    fields = ('title', 'short_description', 'long_description', 'longitude', 'latitude',)
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('number', 'place',)
    list_display_links = ('number', 'place',)
