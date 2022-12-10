"""
Definition of views.
"""
from django.shortcuts import redirect ,render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
def index(request):
    return render(request,"app/index.html")
def signup(request):
    if request.method=="POST":
        username=request.POST["username"]
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]
        if User.objects.filter(username=username):
            messages.error(request,"Username already existed!")
            return redirect("home")
        if User.objects.filter(email=email):
            messages.error(request,"Email address already existed")
            return redirect("home")
        if len(username)>10:
            messages.error(request,"username must be under 10 chrachters")
        if pass1!=pass2:
            messages.error(request,"Password not matched!!")
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname 
        myuser.save()
        messages.success(request,"Your account has been successfully created")
        subject="Welcome to teh website!"
        message="Hello" + myuser.first_name
        to_list=[myuser.email]
        send_mail(subject,message,to_list,fail_silently=True)
        return redirect("signin")
    return render(request,"app/signup.html")
def signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        pass1=request.POST["pass1"]
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"authentication/index.html",{"fname":fname})
        else:
            messages.error(request,"Wrong Credentials")
            return redirect("home")
    return render(request,"app/signin.html")
def signout(request):
    logout(request)
    messages.success(request,"logged out successfully")
    return redirect("home")

