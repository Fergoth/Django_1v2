from adminsortable2.admin import (
    SortableAdminBase,
    SortableAdminMixin,
    SortableStackedInline,
)
from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, PlaceImage


class ImageInline(SortableStackedInline):
    model = PlaceImage

    readonly_fields = ['preview']
    fields = ('image', 'preview', 'order')
    extra = 1

    def preview(self, obj):
        max_height = 200
        if obj.image.height >= max_height:
            height = max_height
            width = int(obj.image.width * (max_height/obj.image.height))
        else:
            height = obj.image.height
            width = obj.image.width
        return format_html(
            '<img src="{url}" width="{width}" height={height} />'.
            format(
                url=obj.image.url,
                width=width,
                height=height,
            )
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline,]
    search_fields = ['title']
