from django.contrib import admin
from .models import CommentModel


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['author', 'comment', 'created_at']
    ordering = ['created_at']

admin.site.register(CommentModel, CommentsAdmin)
