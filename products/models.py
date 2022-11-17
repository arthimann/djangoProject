from django.db import models
from categories.models import Categories


class Products(models.Model):
    category_id = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
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

