from django.shortcuts import render
from django.shortcuts import redirect
from .models import DriveRequest, Car
from accounts.models import Profile
from . import views

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('loginpage')

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
            numOfBaggage = request.POST['baggage'],
        )
        
        make = request.POST['carMake']
        model = request.POST['carModel']
        year = request.POST['carYear']

        if make and model and year:
            car = Car.objects.create(
                Make = make,
                Model = model,
                Year = year
            )
            
            car.save()
            
            driveRequest_instance.Car = car
            driveRequest_instance.save()
        
        print(request.user)
		
        driveRequest_instance.Rider = request.user

        driveRequest_instance.save()

    driveRequests = DriveRequest.objects.all()
    print("driveRequests:")
    print(driveRequests)

    return render(request,"driver_page.html",{'driveRequests':driveRequests})

def ridepopup(request):
    return render(request,'ridePopup.html')

def profile(request):
    return render(request, 'profile.html');
