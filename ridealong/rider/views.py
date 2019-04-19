from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import RideRequest
from driver.models import DriveRequest, RiderLink
from accounts.models import Profile
from . import views
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    if not request.user.is_authenticated:
        return redirect('loginpage')

    riderLinks = RiderLink.objects.filter(Rider = request.user)
    driveRequests = DriveRequest.objects.exclude(pk__in = riderLinks.values_list("DriveRequest", flat=True)).order_by("-RequestTime")[:30]
    
    if request.method == "GET":
        if request.GET.get("searchButton") is not None:
            return riderSearch(request)
        elif request.GET.get("removeRequestButton") is not None:
            if RiderLink.objects.filter(ID = request.GET["removeRequestButton"]):
                RiderLink.objects.get(ID = request.GET["removeRequestButton"]).delete()
            
            return render(request,"rider_page.html",{'riderLinks':riderLinks, 'driveRequests':driveRequests})
        elif request.GET.get("requestButton") is not None:
            driveRequest = DriveRequest.objects.get(ID = request.GET["requestButton"])
            
            
            #User wants to request ride with ID driveReqID
            #First, we need to check if they've already requested this ride (we should actually do this before rendering the page...)
            #If not, we need to create a new RiderLink and email the Rider and Driver. Then when the Rider loads this page again, they'll see
            #that they've requested the given ride, as well as if it's been accepted or denied. The driver will also see this stuff on their page.
            
            if RiderLink.objects.filter(DriveRequest = driveRequest):
                #User has already requested this, so we just return to the page.
                return render(request,"rider_page.html",{'isIndex':True,'riderLinks':riderLinks, 'driveRequests':driveRequests})
            
            riderLink = RiderLink.objects.create(
                Rider = request.user,
                DriveRequest = driveRequest,
            )
            subject1 = 'Request Received.'
            message1 = 'Your ride request has been received, and the driver has been notified!'
            email_from1 = settings.EMAIL_HOST_USER
            recipient1 = request.user.profile.ContactEmail
            recipient_list = [recipient1,] 
            send_mail(subject1, message1, email_from1, recipient_list)
            subject1 = 'Someone wants to ride with you!'
            message1 = 'A user has requested to ride with you. Check the site for more details!'
            email_from1 = settings.EMAIL_HOST_USER
            recipient1 = driveRequest.Rider.profile.ContactEmail
            print(recipient1)
            recipient_list = [recipient1,] 
            send_mail(subject1, message1, email_from1, recipient_list)
            
            riderLinks = RiderLink.objects.filter(Rider = request.user)
            driveRequests = DriveRequest.objects.exclude(pk__in = riderLinks.values_list("DriveRequest", flat=True)).order_by("-RequestTime")[:30]
    
            return render(request,"rider_page.html",{'requestSuccess':True,'riderLinks':riderLinks, 'driveRequests':driveRequests})
    #print (times)
    
    return render(request,"rider_page.html",{'isIndex':True,'riderLinks':riderLinks, 'driveRequests':driveRequests})

def rides1(request):
    rideRequests = RideRequest.objects.all()
    return render(request,"rides1.html",{'isIndex':True,'rideRequests':rideRequests})

def riderSearch(request):
    print("IN RIDER SEARCH")
    #ex. query http://localhost:8000/driver/search?searchLocation=West&filter=location
    #ex. query for date http://localhost:8000/driver/search?searchYear=2222&searchMonth=2&searchDay=2&filter=date
    #filter options: location,date,price,luggage,passengershttp://localhost:8000/driver/search?Filter=Price
    if request.method == "GET":
        print (request.GET)
        if request.GET['filter'] == 'location':
            searchResult = DriveRequest.objects.filter(departLoc__search=request.GET['originLocation'],arrivalLoc__search=request.GET['destLocation'])
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

def ridernotfications(request):
    return render (request,'ridernotifications.html')
    