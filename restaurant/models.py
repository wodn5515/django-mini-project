from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(_("음식점 이름"), max_length=255)
    description = models.CharField(_("음식점 소개"), max_length=255)
    address = models.CharField(_("음식점 주소"), max_length=255)
    phone_number = models.CharField(_("음식점 전화번호"), max_length=255)

    class Meta:
        db_table = _("restaurant")
        verbose_name = _("음식점")
        verbose_name_plural = _("음식점")

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="menus")
    name = models.CharField(_("메뉴 이름"), max_length=255)
    price = models.IntegerField(_("메뉴 가격"))

    class Meta:
        db_table = _("menu")
        verbose_name = _("메뉴")
        verbose_name_plural = _("메뉴")