from django.db import models
from products.models import Product


class Comment(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', db_column='product_id')
    author = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'
        index_together = (
            ('created_at', 'updated_at')
        )
