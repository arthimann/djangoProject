from django.db import models
from products.models import ProductModel
from . import constants


class CommentModel(models.Model):
    product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name=constants.RELATED_NAME,
                                   db_column=constants.FOREIGN_KEY_DB_COLUMN)
    author = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = constants.DB_TABLE
        index_together = (
            (constants.COL_NAME_CREATED_AT, constants.COL_NAME_UPDATED_AT)
        )
        verbose_name = constants.VERBOSE_NAME
