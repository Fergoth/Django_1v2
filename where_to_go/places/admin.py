from adminsortable2.admin import (
    SortableAdminBase,
    SortableStackedInline,
    SortableAdminMixin
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
        max_width = 200
        return format_html(
            '<img src="{}" style="max-height: {}px; max-width: {}px;" />',  # noqa: E501
            obj.image.url,
            max_height,
            max_width
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline,]
    search_fields = ['title']


@admin.register(PlaceImage)
class PlaceImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    raw_id_fields = ['place']
