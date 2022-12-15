from django.contrib import admin
from .models import CategoryModel


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    ordering = ['created_at']


admin.site.register(CategoryModel, CategoriesAdmin)
