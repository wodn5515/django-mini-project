from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RestaurantListSerializer, RestaurantCreateSerializer, RestaurantDetailSerializer, MenuSerializer
from .paginations import StandardPagination
from .models import Restaurant, Menu

class RestaurantListCreateView(ListCreateAPIView):
    pagination_class = StandardPagination

    # 요청된 method 에 따른 serializer class 가져오기
    def get_serializer_class(self):
        if self.request.method == "GET":
            return RestaurantListSerializer
        return RestaurantCreateSerializer

    def get_queryset(self):
        return Restaurant.objects.values("id", "name", "address", "phone_number").all()


class RestaurantRetrieveView(RetrieveAPIView):
    serializer_class = RestaurantDetailSerializer
    queryset = Restaurant.objects.prefetch_related("menus").all()


class MenuCreateView(CreateAPIView):
    serializer_class = MenuSerializer

    def perform_create(self, serializer):
        restaurant = Restaurant.objects.get(pk=self.kwargs["pk"])
        serializer.save(restaurant=restaurant)