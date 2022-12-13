from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>/store/', views.store_view, name='comment_store'),
]
