from django.shortcuts import render

# Create your views here.

def index(request):
    print(request.GET['departLoc'])
    return render(request,"driver_page.html")

def storeRideInfo(request):
    return

def ridepopup(request):
    return render(request,'ridePopup.html')


