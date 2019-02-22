from django.shortcuts import render
from . import models

# Create your views here.

def index(request):
    print (request.method)
    if request.method == "POST":
        print(request.POST['departLoc'])
        print(request.POST['arrivalLoc'])
        print(request.POST['pickupTime'])
        print(request.POST['dropTime'])
        print(request.POST['seats'])
        print(request.POST['baggage'])

    return render(request,"driver_page.html")

def ridepopup(request):
    return render(request,'ridePopup.html')


