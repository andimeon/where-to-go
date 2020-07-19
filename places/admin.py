from django.contrib import admin
from .models import Place, Image
from django.utils.safestring import mark_safe
import traceback
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image

    try:
        readonly_fields = ['preview_image']
    except Exception:
        pass
    print (traceback.print_exc)

    fields = ('image', 'preview_image', 'position')

    def preview_image(self, instance):
        return format_html(
            mark_safe('<img src="{url}" width="225" height="150" />'.format(
            url = instance.image.url)))

class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title']

    inlines = [
        ImageInline,
    ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image)