from django.contrib import admin
from .models import ProductModel


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_at']
    ordering = ['created_at']


admin.site.register(ProductModel, ProductsAdmin)
