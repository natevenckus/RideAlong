from django.shortcuts import render
from django.shortcuts import redirect
from .models import RideRequest
from accounts.models import Profile
from . import views

def index(request):
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