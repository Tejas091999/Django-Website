''''app urls'''

from django.urls import path,include
from django.contrib import admin
from . import views



urlpatterns =[        
path("",views.index,name="index"),
path("signup",views.signup,name="signup"),
path("signin",views.signin,name="signin"),
path("signout",views.signout,name="signout")
]
 
