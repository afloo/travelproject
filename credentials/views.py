from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method =='POST':
        usrnm=request.POST['Username']
        paswd=request.POST['Password']
        user=auth.authenticate(username=usrnm,password=paswd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        usrnm=request.POST['Username']
        fstnm=request.POST['First_name']
        lstnm=request.POST['Last_name']
        email=request.POST['Email']
        pswd=request.POST['Password']
        cpswd=request.POST['C_Password']
        if pswd==cpswd:
            if User.objects.filter(username=usrnm).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email taken")
                return redirect('register')
            user=User.objects.create_user(username=usrnm,password=pswd,first_name=fstnm,last_name=lstnm,email=email)

            user.save();
            print("User created")
            return redirect('login')
        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')