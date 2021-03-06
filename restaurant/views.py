from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt

from .models import Menu, Restaurant

import json


# Create your views here.

############################ Function Based View ###########################

@csrf_exempt
@require_http_methods(["GET", "POST"])
def restaurant_create_list(request):
    if request.method == "GET":
        restaurant = Restaurant.objects.values("id", "name", "address", "phone_number").all()
        paginator = Paginator(restaurant, 20)
        page = int(request.GET.get("page", 1))
        data = paginator.get_page(page)
        return JsonResponse(list(data), safe=False, json_dumps_params={"ensure_ascii":False})
    elif request.method == "POST":
        data = json.loads(request.body)
        new_restaurant = Restaurant(
            name=data.get("name"),
            description=data.get("description"),
            address=data.get("address"),
            phone_number=data.get("phone_number")
        )
        new_restaurant.save()
        obj = model_to_dict(new_restaurant)
        return JsonResponse(obj, json_dumps_params={"ensure_ascii":False}, status=201)

@require_GET
def restaurant_detail(request, pk):
    restaurant = Restaurant.objects.prefetch_related("menus").get(pk=pk)
    menus = []
    for menu in restaurant.menus.all():
        menus.append({"id":menu.id, "name":menu.name, "price":menu.price})
    res = {"id":restaurant.id, "name":restaurant.name, "description":restaurant.description, "address":restaurant.address, "phone_number":restaurant.phone_number, "menus":menus}
    return JsonResponse(res, json_dumps_params={"ensure_ascii":False})

@csrf_exempt
@require_POST
def menu_create(request, pk):
    data = json.loads(request.body)
    restaurant = Restaurant.objects.get(pk=pk)
    new_menu = Menu(
        restaurant=restaurant,
        name=data.get("name"),
        price=data.get("price")
    )
    new_menu.save()
    obj = model_to_dict(new_menu, fields=["id", "name", "price"])
    return JsonResponse(obj, json_dumps_params={"ensure_ascii":False}, status=201)


################################ Class Based View ###############################

@method_decorator(csrf_exempt, name="dispatch")
class RestaurantView(View):
    def get(self, request, *args, **kwargs):
        restaurant = Restaurant.objects.values("id", "name", "address", "phone_number").all()
        paginator = Paginator(restaurant, 20)
        page = int(request.GET.get("page", 1))
        data = paginator.get_page(page)
        return JsonResponse(list(data), safe=False, json_dumps_params={"ensure_ascii":False})

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        new_restaurant = Restaurant(
            name=data.get("name"),
            description=data.get("description"),
            address=data.get("address"),
            phone_number=data.get("phone_number")
        )
        new_restaurant.save()
        obj = model_to_dict(new_restaurant)
        return JsonResponse(obj, json_dumps_params={"ensure_ascii":False}, status=201)


class RestaurantDetailView(View):
    def get(self, request, *args, **kwargs):
        restaurant = Restaurant.objects.prefetch_related("menus").get(pk=kwargs["pk"])
        menus = []
        for menu in restaurant.menus.all():
            menus.append({"id":menu.id, "name":menu.name, "price":menu.price})
        res = {"id":restaurant.id, "name":restaurant.name, "description":restaurant.description, "address":restaurant.address, "phone_number":restaurant.phone_number, "menus":menus}
        return JsonResponse(res, json_dumps_params={"ensure_ascii":False})


@method_decorator(csrf_exempt, name="dispatch")
class MenuCreateView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        restaurant = Restaurant.objects.get(pk=kwargs["pk"])
        new_menu = Menu(
            restaurant=restaurant,
            name=data.get("name"),
            price=data.get("price")
        )
        new_menu.save()
        obj = model_to_dict(new_menu, fields=["id", "name", "price"])
        return JsonResponse(obj, json_dumps_params={"ensure_ascii":False}, status=201)
