from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import RideRequest
from driver.models import DriveRequest
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
    driveRequests = DriveRequest.objects.all()
    #times = DriveRequest.objects.all().values_list('pickupTime',flat=True)
    #print (times)
    print("rideRequests:")
    print(rideRequests)
    return render(request,"rider_page.html",{'isIndex':True,'driveRequests':driveRequests})
    
    return render(request,'rider_page.html')

def rides1(request):
    rideRequests = RideRequest.objects.all()
    return render(request,"rides1.html",{'isIndex':True,'rideRequests':rideRequests})

def riderSearch(request):
    #ex. query http://localhost:8000/driver/search?searchLocation=West&filter=location
    #ex. query for date http://localhost:8000/driver/search?searchYear=2222&searchMonth=2&searchDay=2&filter=date
    #filter options: location,date,price,luggage,passengershttp://localhost:8000/driver/search?Filter=Price
    if request.method == "GET":
        print (request.GET)
        if request.GET['filter'] == 'location':
            searchResult = DriveRequest.objects.filter(departLoc__search=request.GET['searchLocation'])
        elif request.GET['filter'] == 'date':
            date = request.GET['departDate'].split('-')
            searchResult = DriveRequest.objects.filter(pickupTime__year=int(date[0]), pickupTime__month=int(date[1]),pickupTime__day=int(date[2]))
        elif request.GET['filter'] == 'price':
            q = SearchQuery(request.GET['searchPrice'])
            vector = SearchVector(Cast('PriceOffer', CharField()))
            searchResult=DriveRequest.objects.annotate(search=vector).filter(search=q)
        elif request.GET['filter'] == 'luggage':
            q = SearchQuery(request.GET['searchLuggage'])
            vector = SearchVector(Cast('numOfBaggage', CharField()))
            searchResult=DriveRequest.objects.annotate(search=vector).filter(search=q)
        elif request.GET['filter'] == 'passenger':
            searchResult=DriveRequest.objects.annotate(search=vector).filter(search=q)

    return render(request,"show_rides.html",{'isIndex':False,'searchResult':searchResult})

    
def deleteride(request):
    if not request.GET['id']:
        return HttpResponse("No ID")
    
    RideRequest.objects.filter(ID=request.GET['id']).delete()
    return redirect('rides1')

#def rider(request):
    #return render(request,'rider_page.html')

#def driver(request):
    #return render(request,'driver_page.html')
    
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
    