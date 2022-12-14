from django.db import models
from categories.models import CategoryModel


class ProductModel(models.Model):
    category_id = models.ForeignKey(CategoryModel, on_delete=models.DO_NOTHING, db_column='category_id')
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'
        index_together = (
            ('created_at', 'updated_at')
        )
        verbose_name = 'Product'
