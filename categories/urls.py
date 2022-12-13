from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='categories_index'),
    path('store/', views.store_view, name='categories_store'),
]
