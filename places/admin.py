from django.contrib import admin
from .models import Place, Image
from django.utils.safestring import mark_safe
import traceback
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ['place']


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image

    try:
        readonly_fields = ['preview_image']
    except Exception:
        pass

    fields = ('image', 'preview_image', 'position')

    def preview_image(self, instance):
        return format_html('<img src="{0}" width="225" height="150" />', instance.image.url)

class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

    inlines = [
        ImageInline,
    ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image, ImageAdmin)