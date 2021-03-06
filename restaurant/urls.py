from django.urls import path

from . import views

urlpatterns = [
    path("restaurant", views.restaurant_create_list),
    path("restaurant/<int:pk>", views.restaurant_detail),
    path("restaurant/<int:pk>/menu", views.menu_create)
]
