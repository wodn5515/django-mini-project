from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET
from django.views.decorators.csrf import csrf_exempt

from .models import Menu, Restaurant

import json


# Create your views here.
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
        return HttpResponse(json.dumps(obj, ensure_ascii=False), content_type="application/json", status=201)

@require_GET
def restaurant_detail(request, pk):
    data = Restaurant.objects.values("id", "name", "description", "address", "phone_number").get(pk=pk)
    return JsonResponse(data, json_dumps_params={"ensure_ascii":False})