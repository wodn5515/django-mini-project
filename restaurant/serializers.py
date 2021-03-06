from rest_framework import serializers as sz

from .models import Restaurant, Menu

class RestaurantCreateSerializer(sz.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = "__all__"


class RestaurantListSerializer(sz.ModelSerializer):

    class Meta:
        model = Restaurant
        exclude = ("description",)


class MenuSerializer(sz.ModelSerializer):

    class Meta:
        model = Menu
        fields = ["id", "name", "price"]
        read_only_fields = ["restaurant"]


class RestaurantDetailSerializer(sz.ModelSerializer):
    menus = MenuSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = "__all__"

