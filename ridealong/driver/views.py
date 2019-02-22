from django.shortcuts import render
from .models import DriveRequest

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
        driveRequest_instance = DriveRequest.objects.create(
            departLoc = request.POST['departLoc'],
            arrivalLoc = request.POST['arrivalLoc'],
            pickupTime = request.POST['pickupTime'],
            dropTime = request.POST['dropTime'],
            numOfSeats = request.POST['seats'],
            numOfBaggage = request.POST['baggage']
        )
        driveRequest_instance.save()

    return render(request,"driver_page.html")

def ridepopup(request):
    return render(request,'ridePopup.html')

def profile(request):
    return render(request, 'profile.html');
