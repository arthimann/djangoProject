from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='products_index'),
    path('<int:product_id>/', views.show_view, name='products_show'),
    path('store/', views.store_view, name='products_store'),
    path('<int:product_id>/edit/', views.edit_view, name='products_edit'),
]
