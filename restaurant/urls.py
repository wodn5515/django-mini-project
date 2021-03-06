from django.urls import path
from . import views

urlpatterns = [
    path("restaurant", views.restaurant_create_list),
    path("restaurant/<int:pk>", views.restaurant_detail)
]
