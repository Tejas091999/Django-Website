"""
Definition of urls for Mysite.
"""


from django.urls import path,include
from django.contrib import admin


urlpatterns = [
    path("admin/",admin.site.urls),
    path("food/",include("food.url")),
]
