from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from adminsortable2.admin import SortableAdminBase, SortableAdminMixin, SortableTabularInline

from .models import Image, Place


def get_preview(image_url, max_height=200):
    return format_html(mark_safe(f'<img src="{image_url}" style="max-height: {max_height}px;">'))


class ImageInline(SortableTabularInline):
    model = Image
    fields = ('number', 'image', 'preview',)
    readonly_fields = ('preview',)

    def preview(self, obj):
        return get_preview(obj.image.url)

    preview.short_description = 'Предпросмотр'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]    
    fields = ('title', 'short_description', 'long_description', 'longitude', 'latitude', 'id',)
    list_display = ('title',)
    list_display_links = ('title',)
    readonly_fields = ('id',)
    search_fields = ('title',)


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    fields = ('place', 'number', 'image', 'preview',)
    list_display = ('number', 'id', 'place', 'small_preview',)
    list_display_links = ('number', 'place',)
    readonly_fields = ('preview',)

    def preview(self, obj):
        return get_preview(obj.image.url)

    preview.short_description = 'Предпросмотр'

    def small_preview(self, obj):
        return get_preview(obj.image.url, max_height=50)

    small_preview.short_description = 'Фото'
