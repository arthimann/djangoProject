from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('add/', views.add_view, name='create'),
]
