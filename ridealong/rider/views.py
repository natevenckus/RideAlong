from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import RideRequest
from accounts.models import Profile
from . import views

def index(request):
    print("IN RIDER INDEX!!!")

    if not request.user.is_authenticated:
        return redirect('loginpage')
    
    if request.method == "POST":
        departLoc = request.POST['departLoc']
        arrivalLoc = request.POST['arrivalLoc']
        pickupTime = request.POST['pickupTime']
        dropTime = request.POST['dropTime']
        numOfSeats = request.POST['seats']
        numOfBaggage = request.POST['baggage']
    
        if departLoc and arrivalLoc and pickupTime and dropTime and numOfSeats and numOfBaggage:
            rideRequest_instance = RideRequest.objects.create(
                departLoc = request.POST['departLoc'],
                arrivalLoc = request.POST['arrivalLoc'],
                pickupTime = request.POST['pickupTime'],
                dropTime = request.POST['dropTime'],
                seatsNeeded = request.POST['seats'],
                baggageNeeded = request.POST['baggage'],
            )
            rideRequest_instance.save()
            
        rideRequest_instance.Rider = request.user

        rideRequest_instance.save()

    rideRequests = RideRequest.objects.all()
    #times = DriveRequest.objects.all().values_list('pickupTime',flat=True)
    #print (times)
    print("rideRequests:")
    print(rideRequests)
    return render(request,"rider_page.html",{'isIndex':True,'rideRequests':rideRequests})
    
    return render(request,'rider_page.html')

def rides(request):
    rideRequests = RideRequest.objects.all()
    return render(request,"rides.html",{'isIndex':True,'rideRequests':rideRequests})
    
def deleteride(request):
    if not request.GET['id']:
        return HttpResponse("No ID")
    
    RideRequest.objects.filter(ID=request.GET['id']).delete()
    return redirect('rides')

def rider(request):
    return render(request,'rider_page.html')

def driver(request):
    return render(request,'driver_page.html')
    
def updateride(request):
    id = request.GET['id']
    departLoc = request.GET['departLoc']
    arrivalLoc = request.GET['arrivalLoc']
    pickupTime = request.GET['pickupTime']
    seatsNeeded = request.GET['seats']
    baggageNeeded = request.GET['baggage']
    
    print("THE DATE")
    print(request.GET['pickupTime'])
    
    ride = RideRequest.objects.filter(ID=id)[0]
    
    ride.departLoc = departLoc
    ride.arrivalLoc = arrivalLoc
    ride.pickupTime = pickupTime
    ride.seatsNeeded = seatsNeeded
    ride.baggageNeeded = baggageNeeded
    
    ride.save()
    
    return redirect('rides')
    