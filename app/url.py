#App url
from django.urls import path
from django.contrib import admin
from app import views

urlpatterns = [
path("",views.index,name="home"),
path("about",views.about,name="about"),
path("services",views.services,name="services"),
path("contact",views.contact,name="contact"),
path("cone",views.cone,name="cone"),
path("family",views.family,name="family")
]

