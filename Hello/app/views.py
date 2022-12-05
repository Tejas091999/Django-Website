"""
Definition of views.
"""


from http.client import HTTPResponse
from django.shortcuts import render ,HttpResponse


def index(request):
    context={
        'variable':"Tis is sent"}
    return render(request,"index.html",context)
    #return HttpResponse("This is home page.")
def about(request):
    return render(request,"about.html")
def services(request):
    return render(request,"services.html")
def contact(request):
    return render(request,"contact.html")
def cone(request):
    return render(request,"cone.html")
def family(request):
    return render(request,"family.html")



