from django.contrib import admin
from django.utils.html  import format_html
from django.utils.safestring import mark_safe

from .models import Image, Place


class ImageInline(admin.TabularInline):
    model = Image
    fields = ('image', 'preview', 'number',)
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            return format_html(mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">'))
    preview.short_description = 'Предпросмотр'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]    
    fields = ('title', 'short_description', 'long_description', 'longitude', 'latitude',)
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ('place', 'number', 'image', 'preview',)
    list_display = ('number', 'place',)
    list_display_links = ('number', 'place',)
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            return format_html(mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">'))
    preview.short_description = 'Предпросмотр'
