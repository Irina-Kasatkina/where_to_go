from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from adminsortable2.admin import SortableAdminBase, SortableAdminMixin, SortableTabularInline

from .models import Image, Place


class ImageInline(SortableTabularInline):
    model = Image
    fields = ('number', 'image', 'preview',)
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            return format_html(mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">'))
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
        if obj.image:
            return format_html(mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">'))
    preview.short_description = 'Предпросмотр'

    def small_preview(self, obj):
        if obj.image:
            return format_html(mark_safe(f'<img src="{obj.image.url}" style="max-height: 50px;">'))
    small_preview.short_description = 'Фото'
