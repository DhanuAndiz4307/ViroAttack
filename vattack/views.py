from django.shortcuts import redirect, render
# from .models import Destination
from django.http.response import HttpResponse
from django.contrib.auth.models import User, auth
from django.core.checks import messages,Info

# Create your views here.
def Userlogin(request):
        if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            
            user=auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect(homepage)
            else:
                # messages.info(request,'invalid credentials')
                return redirect(Userlogin)
        else:
            return render(request,'Userlogin.html')
    # return HttpResponse("hello")
def signup(request):
    print('Paaaaaaaaaaaaaaaaaaaaarty')
    try:
        # print(request.POST)
        if request.method == "POST":
        
            print(request.POST)
            print('Double Paaaaaaaaaaaaaaaaaaaarty')
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            # username = 'reques'
            # email = 'reques'
            # password1 = 'reque'
            # password2 = 'reque'
        
            user = User.objects.create_user(username=username,password=password1,email=email)
            user.save();
            print('user created')
            return redirect(Userlogin)
        else:
            return render(request,"signup page/signup.html")
    except Exception as e:
        print('Here is your exception  -------@@------------------------',e)
        return HttpResponse("user not registered")

def survey(request):
    return render(request,"signup page/surevy.html")

def homepage(request):
    return render(request,"main page/homepage.html")
def tracking(request):
    return render(request,"main page/tracking.html")
def about(request):
    return render(request,"main page/about.html")
def logout(request):
    auth.logout(request)
    return redirect(Userlogin)