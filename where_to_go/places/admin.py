from django.contrib import admin
from django.utils.html import format_html
from places.models import Place, Image
from adminsortable2.admin import SortableAdminMixin


class ImageInline(admin.TabularInline):
    model = Image

    readonly_fields = ['preview']
    fields = ('image', 'preview', 'order')

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
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline,]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
