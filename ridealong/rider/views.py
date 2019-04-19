from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import RideRequest
from driver.models import DriveRequest, RiderLink
from accounts.models import Profile
from . import views
from django.core.mail import send_mail
from django.conf import settings
import json,requests
from math import radians, sin, cos, acos

#https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=40.4309891,%20-86.9169804&destinations=40.4003151,%20-86.8634453&key=AIzaSyAwAf6GdGjSHj7yjhWXaFdr7F6T09PPMJk
#calculate distance between two geocoordinates
def withinRadius(xLat,xLong,yLat,yLong,radius):
    requestURL = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="+str(xLat)+","+str(xLong)+"&destinations="+str(yLat)+","+str(yLong)+"&key="+googleKey
    response = requests.get(requestURL)
    json_response = json.loads(response.text)
    distance = json_response['rows'][0]['elements'][0]['distance']['text']
    radius = float(radius)
    if distance[-2:] == 'ft':
        return True
    try:
        distance = float(distance[:-3])
    except ValueError:
        return False
    if( distance < radius):
        return True


#https://maps.googleapis.com/maps/api/geocode/json?address=1600%20Amphitheatre%20Pkwy,%20Mountain%20View,%20CA%2094043,%20USA&key=AIzaSyAwAf6GdGjSHj7yjhWXaFdr7F6T09PPMJk
googleKey = 'AIzaSyAwAf6GdGjSHj7yjhWXaFdr7F6T09PPMJk'

#return geocoordinates [originLat, originLong, destLat, destLong]
#from address
def getGeo(originAddress, destAddress):
    coordinates=[]
    originRequest = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + originAddress+'&fields=geometry&key='+googleKey
    destRequest = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + destAddress+'&fields=geometry&key='+googleKey
    originResponse = requests.get(originRequest)
    destResponse = requests.get(destRequest)
    origin_json = json.loads(originResponse.text)
    dest_json = json.loads(destResponse.text)
    coordinates.append(origin_json['results'][0]['geometry']['location']['lat'])
    coordinates.append(origin_json['results'][0]['geometry']['location']['lng'])
    coordinates.append(dest_json['results'][0]['geometry']['location']['lat'])
    coordinates.append(dest_json['results'][0]['geometry']['location']['lng'])
    return (coordinates)


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
            if RiderLink.objects.filter(DriveRequest = driveRequest).filter(Rider = request.user):
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
        if request.GET['filter'] == 'location':
            radius = request.GET['radius']
            riderLinks = RiderLink.objects.filter(Rider = request.user)
            driveRequests = DriveRequest.objects.exclude(pk__in = riderLinks.values_list("DriveRequest", flat=True)).order_by("-RequestTime")
            coordinatesSearch = getGeo(request.GET['originLocation'],request.GET['destLocation'])
            validRequest=[]
            for drive in driveRequests:
                if drive.FromLat is not None:
                    distanceOrigin = withinRadius(coordinatesSearch[0],coordinatesSearch[1],float(drive.FromLat),float(drive.FromLong),radius)
                    distanceDest = withinRadius(coordinatesSearch[2],coordinatesSearch[3],float(drive.ToLat),float(drive.ToLong),radius)
                    if distanceOrigin and distanceDest:
                        validRequest.append(drive.ID)
            searchResult = DriveRequest.objects.filter(ID__in=validRequest).order_by('PriceOffer')
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
    rideRequestsR = RiderLink.objects.filter(Rider = request.user)
    currUser = request.user
    return render(request,"ridernotifications.html",{'isIndex':False,'rideRequestsR': rideRequestsR, 'currUser':currUser})
