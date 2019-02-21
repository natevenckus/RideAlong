from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"driver_page.html")

def ridepopup(request):
    return render(request,'ridePopup.html')


