from django.db import models


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        index_together = (
            ('created_at', 'updated_at')
        )
