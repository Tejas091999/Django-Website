#URLS for food

from django.urls import path
from django.contrib import admin
from . import views
app_name="food"
urlpatterns = [
    path("",views.index,name="index"),
    path("item/",views.item,name="item"),
    path("<int:item_id>",views.detail,name="detail"),
    path("add",views.create_item,name="create_item"),
]
