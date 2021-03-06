from django.urls import path

from . import views

urlpatterns = [
    # CBV urls
    path("restaurant", views.RestaurantView.as_view()),
    path("restaurant/<int:pk>", views.RestaurantDetailView.as_view()),
    path("restaurant/<int:pk>/menu", views.MenuCreateView.as_view()),
    # FBV urls
    #path("restaurant", views.restaurant_create_list),
    #path("restaurant/<int:pk>", views.restaurant_detail),
    #path("restaurant/<int:pk>/menu", views.menu_create),
]
