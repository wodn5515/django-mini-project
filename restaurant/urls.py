from django.urls import path,include

from . import views, api

drf_urlpatterns = [
    path("restaurant", api.RestaurantListCreateView.as_view()),
    path("restaurant/<int:pk>", api.RestaurantRetrieveView.as_view()),
    path("restaurant/<int:pk>/menu", api.MenuCreateView.as_view())
]

cbv_urlpatterns = [
    path("restaurant", views.RestaurantView.as_view()),
    path("restaurant/<int:pk>", views.RestaurantDetailView.as_view()),
    path("restaurant/<int:pk>/menu", views.MenuCreateView.as_view())
]

fbv_urlpatterns = [
    path("restaurant", views.restaurant_create_list),
    path("restaurant/<int:pk>", views.restaurant_detail),
    path("restaurant/<int:pk>/menu", views.menu_create)
]

urlpatterns = [
    path("drf/", include(drf_urlpatterns)),
    path("cbv/", include(cbv_urlpatterns)),
    path("fbv/", include(fbv_urlpatterns))
]
