from django.contrib import admin
from .models import GalleryModel


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['file', 'created_at']
    ordering = ['created_at']

admin.site.register(GalleryModel, GalleryAdmin)
