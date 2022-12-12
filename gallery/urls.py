from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='gallery_index'),
    path('create/', views.create_view, name='gallery_create'),
    path('store/', views.store_view, name='gallery_store'),
    path('show/', views.store_view, name='gallery_show'),
    path('destroy/', views.store_view, name='gallery_destroy'),
]
