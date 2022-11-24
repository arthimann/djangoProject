from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>/add/', views.add_view, name='comment_add'),
]
