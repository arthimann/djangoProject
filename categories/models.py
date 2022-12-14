from django.db import models


class CategoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        index_together = (
            ('created_at', 'updated_at')
        )
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
