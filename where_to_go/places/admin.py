from django.contrib import admin
from places.models import Place


@admin.register(Place)
class CommentAdmin(admin.ModelAdmin):
    pass
