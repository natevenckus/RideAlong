from django.shortcuts import render
from django.shortcuts import redirect
from .models import RiderRequest, Car
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
        
        departLoc = request.POST['departLoc']
        arrivalLoc = request.POST['arrivalLoc']
        pickupTime = request.POST['pickupTime']
        dropTime = request.POST['dropTime']
        numOfSeats = request.POST['seats']
        numOfBaggage = request.POST['baggage']
        
        if departLoc and arrivalLoc and pickupTime and dropTime and numOfSeats and numOfBaggage:
            riderRequest_instance = RiderRequest.objects.create(
                departLoc = request.POST['departLoc'],
                arrivalLoc = request.POST['arrivalLoc'],
                pickupTime = request.POST['pickupTime'],
                dropTime = request.POST['dropTime'],
                numOfSeats = request.POST['seats'],
                numOfBaggage = request.POST['baggage'],
            )
            
            riderRequest_instance.save()
        
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
            
            riderRequest_instance.Car = car
            riderRequest_instance.save()
            
        deleteID = request.POST['deleteID']
        editID = request.POST['editID']
        editField = request.POST['editField']
        editVal = request.POST['editVal']
       
        if deleteID:
            print("delete record here")
        
        if editID and editField and editVal:
            print("edit record here")
        
        print(request.user)
		
        riderRequest_instance.Rider = request.user

        riderRequest_instance.save()

    riderRequests = riderRequest.objects.all()
    print("riderRequests:")
    print(riderRequests)

    return render(request,"rider_page.html",{'riderRequests':riderRequests})

def ridepopup(request):
    return render(request,'ridePopup.html')

def profile(request):
    return render(request, 'profile.html')

