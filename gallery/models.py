from django.db import models

# Create your models here.
class GalleryModel(models.Model):
    file = models.FileField(upload_to='images/', null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'gallery'
        index_together = (
            ('created_at', 'updated_at'),
        )
