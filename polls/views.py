from django.contrib import messages
from django.shortcuts import redirect, render, HttpResponse
from .models import TENDERER, Tender, OEM, BIDDER
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import TenderForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, tender_name):
    room = Tender.objects.get(id=tender_name)
    context = {'room' : room}
    return render(request, 'room.html', context)

def register(request):
    return render(request, 'register.html')

def user(request):
    if (request.method == "POST"):
        username = request.POST["logname"]
        password = request.POST["logpass"]
        email = request.POST["logemail"]
        fname = request.POST["log_as"]

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('register')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('register')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('register')

        
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = fname

        myuser.save()
        messages.success(request, "Succesfully Registered!")

        if (fname == "oem"):
            b = OEM(username=username, email=email)
            b.save()
            print("------------------------", fname, OEM.objects.all())

        if (fname == "tenderer"):
            b = TENDERER(username=username, email=email)
            b.save()
            print("------------------------", fname, TENDERER.objects.all())

        if (fname == "bidder"):
            b = BIDDER(username=username, email=email)
            b.save()
            print("------------------------", fname, BIDDER.objects.all())
        

        return redirect('register')
        
    return render(request, 'user')

def signin(request):
    if(request.method == "POST"):
        username = request.POST["username"]
        password = request.POST['logpass']
        fname_s = request.POST['log_as']

        user = authenticate(username=username, password=password)
        if user is not None:
            fname = user.first_name
            username = user.username
            if fname == fname_s:
                login(request, user)
                username = user.username
                if (fname == "tenderer"):
                    print("------------------------", fname, TENDERER.objects.all())
                    return render(request, 'tenderer.html', {"username":username, "login_as":fname})

                if (fname == "bidder"):
                    print("------------------------", fname, BIDDER.objects.all())
                    return render(request, 'bidder.html', {"username":username, "login_as":fname})
                
                if (fname == "oem"):
                    print("------------------------", fname, OEM.objects.all())
                    return render(request, 'oem.html', {"username":username, "login_as":fname})
            else:
                messages.error(request, "No User Registered by username " + username.upper() + " in " + fname_s.upper() + " type!")
                return redirect('register')

        else:
            messages.error(request, "Bad Credentials!")
            return redirect("register")

    return render(request, "register.html")
        
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('register')

def tender_detail(request):
    OEMs = OEM.objects.all()

    contexts = {'OEMS' : OEMs}
    return render(request, 'tender_detail.html', contexts)


def notify(request, pk):
    print("--------------------------------",OEM.objects.filter(id=pk))
    OEM.objects.filter(id=pk).update(notifications=1)
    return render(request, "tender_detail.html")

def tenderer(request):
    form = TenderForm()
    context = {'form':form}
    return render(request, "tenderer.html", context)