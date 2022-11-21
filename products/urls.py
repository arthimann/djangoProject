from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('<int:product_id>/', views.show_view, name='show'),
    path('add/', views.add_view, name='add'),
    path('<int:product_id>/edit/', views.edit_view, name='edit'),
]
