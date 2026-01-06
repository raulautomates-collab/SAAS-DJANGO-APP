from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login

# Create your views here.
def login_view(request):
    username=request.POST['lando']
    password=request.POST['123']
    user=authenticate(request,user=username,password=password)
    if user is not None:
        login(request,user)
        return redirect('/')
    return render(request,'userlogin.html')