"""
Definition of urls for Hello.
"""
#Project url

from django.urls import include,path
from django.contrib import admin


urlpatterns = [
    path('admin/',admin.site.urls),
    path("",include("app.url"))

]
