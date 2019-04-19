from django.shortcuts import render
from django.shortcuts import redirect
from .models import DriveRequest, Car, RiderLink
from accounts.models import Profile
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.db.models.functions import Cast
from django.db.models import CharField
from . import views
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import json, requests

#https://maps.googleapis.com/maps/api/place/details/output?parameters
#https://maps.googleapis.com/maps/api/place/details/json?placeid=ChIJN1t_tDeuEmsRUsoyG83frY4&fields=name,rating,formatted_phone_number&key=YOUR_API_KEY
#https://maps.googleapis.com/maps/api/place/details/json?placeid=PLACE_ID&fields=geometry&key=AIzaSyAwAf6GdGjSHj7yjhWXaFdr7F6T09PPMJk
googleKey = 'AIzaSyAwAf6GdGjSHj7yjhWXaFdr7F6T09PPMJk'

#return geocoordinates [originLat, originLong, destLat, destLong]
def getGeo(originID, destID):
    coordinates=[]
    originRequest = 'https://maps.googleapis.com/maps/api/place/details/json?placeid=' + originID+'&fields=geometry&key='+googleKey
    destRequest = 'https://maps.googleapis.com/maps/api/place/details/json?placeid=' + destID+'&fields=geometry&key='+googleKey
    originResponse = requests.get(originRequest)
    destResponse = requests.get(destRequest)
    origin_json = json.loads(originResponse.text)
    dest_json = json.loads(destResponse.text)
    coordinates.append(origin_json['result']['geometry']['location']['lat'])
    coordinates.append(origin_json['result']['geometry']['location']['lng'])
    coordinates.append(dest_json['result']['geometry']['location']['lat'])
    coordinates.append(dest_json['result']['geometry']['location']['lng'])
    return (coordinates)


# Create your views here.
@csrf_exempt
def index(request):
    print("IN DRIVER INDEX!!!!!")

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
        print(request.POST['originID'])
        print(request.POST['destID'])
        originID = request.POST['originID']
        destID = request.POST['destID']
        departLoc = request.POST['departLoc']
        arrivalLoc = request.POST['arrivalLoc']
        pickupTime = request.POST['pickupTime']
        dropTime = request.POST['dropTime']
        numOfSeats = request.POST['seats']
        numOfBaggage = request.POST['baggage']
        priceOffer = request.POST['Price']
        if destID and originID and departLoc and arrivalLoc and pickupTime and dropTime and numOfSeats and numOfBaggage and priceOffer:
            coordinates = getGeo(originID,destID)
            print (coordinates)
            driveRequest_instance = DriveRequest.objects.create(
                Rider = request.user,
                departLoc = request.POST['departLoc'],
                arrivalLoc = request.POST['arrivalLoc'],
                pickupTime = request.POST['pickupTime'],
                dropTime = request.POST['dropTime'],
                numOfSeats = request.POST['seats'],
                numOfBaggage = request.POST['baggage'],
                PriceOffer = request.POST['Price'],
                FromLat = coordinates[0],
                FromLong = coordinates[1],
                ToLat = coordinates[2],
                ToLong = coordinates[3]
            )
            print (driveRequest_instance.FromLat)
            driveRequest_instance.save()
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
        """
        deleteID = request.POST['deleteID']
        editID = request.POST['editID']
        editField = request.POST['editField']
        editVal = request.POST['editVal']
        if deleteID:
            print("delete record here")
        if editID and editField and editVal:
            print("edit record here")
        """
        print(request.user)
        driveRequest_instance.Rider = request.user
        driveRequest_instance.save()
        return render(request,"create_ride.html");

    driveRequests = DriveRequest.objects.all()
    #times = DriveRequest.objects.all().values_list('pickupTime',flat=True)
    #print (times)
    print("driveRequests:")
    print(driveRequests)
    return render(request,"driver_page.html",{'isIndex':True,'driveRequests':driveRequests})

def rides(request):
    if not request.user.is_authenticated:
        return redirect('loginpage')
    driveRequests = DriveRequest.objects.filter(Rider = request.user)
    links = RiderLink.objects.filter(DriveRequest__in = driveRequests)
    
    if request.method == "GET":
        if request.GET.get("Update") is not None:
            print("UPDATING")
            return updateride(request)
        if request.GET.get("choiceSubmit") is not None:
            linkID = request.GET["choiceSubmit"]
            rl = RiderLink.objects.get(ID = linkID)
                
            if request.GET["Choice"] == "Accept":
                print("ACCEPT")
                rl.Confirmed = True
                rl.Denied = False
                rl.ConfirmedTime = datetime.now()
                rl.save()
                subject1 = 'Your Ride was Accepted!'
                message1 = 'Congratulations! Your ride was accepted!Log into the RideAlong website for more details!- RideAlong Team'
                email_from1 = settings.EMAIL_HOST_USER
                recipient1 = rl.Rider.profile.ContactEmail
                recipient_list = [recipient1,]
                send_mail(subject1, message1, email_from1, recipient_list)

            elif request.GET["Choice"] == "Decline":
                print("DECLINE")
                rl.Denied = True
                rl.Confirmed = False
                rl.DeniedTime = datetime.now()
                rl.save()
                subject1 = 'Your Ride was Declined'
                message1 = 'I am sorry. Your ride was declined. Please log into RideAlong website to find another ride. We apologize for the inconvenience - RideAlong Team '
                email_from1 = settings.EMAIL_HOST_USER
                recipient1 = rl.Rider.profile.ContactEmail
                recipient_list = [recipient1,]
                send_mail(subject1, message1, email_from1, recipient_list)
    
    return render(request,"rides.html",{'isIndex':True,'driveRequests':driveRequests, 'rideRequests': links})

def driverSearch(request):
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
    return render(request,"driver_page.html",{'isIndex':False,'searchResult':searchResult})

def ridepopup(request):
    return render(request,'ridePopup.html')

#def rider(request):
    #return render(request,'rider_page.html')

#def driver(request):
    #return render(request,'driver_page.html')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('loginpage')
    profileSet = Profile.objects.filter(pk=request.user.profile.pk)
    return render(request,"profile.html",{'profilePage':profileSet})

def saveprofile(request):
    id = request.GET['id']

    prof = Profile.objects.filter(id=id)[0]
    prof.SchoolName = request.GET['school']
    prof.FullName = request.GET['name']
    #prof.Car = request.GET['car']
    #print(request.GET['car']);
    prof.save()
    return redirect('/driver/profile')

def drivernotfications(request):
    driveRequests2 = DriveRequest.objects.filter(Rider = request.user)
    rideRequests2 = RiderLink.objects.filter(DriveRequest__in = driveRequests2)
   #rideRequests2Confirmed = rideRequests2.objects.filter(Confirmed = True)
    #rideRequests2Denied = rideRequests2.objects.filter(Denied = True)
    #return render(request,"drivernotifications.html",{'isIndex':False,'driveRequests2':driveRequests2,'rideRequests2': rideRequests2,'confirmed2':rideRequests2Confirmed,'denied2':rideRequests2Denied})
    return render(request,"drivernotifications.html",{'isIndex':False,'driveRequests2':driveRequests2,'rideRequests2': rideRequests2})

def updateride(request):
    id = request.GET['Update']
    print(id)
    departLoc = request.GET['departLoc']
    arrivalLoc = request.GET['arrivalLoc']
    pickupTime = request.GET['pickupTime']
    seatsNeeded = request.GET['seats']
    baggageNeeded = request.GET['baggage']
    
    print("THE DATE")
    print(request.GET['pickupTime'])
    
    ride = DriveRequest.objects.get(ID=id)
    
    ride.departLoc = departLoc
    ride.arrivalLoc = arrivalLoc
    ride.pickupTime = pickupTime
    ride.seatsNeeded = seatsNeeded
    ride.baggageNeeded = baggageNeeded
    
    ride.save()
    
    return redirect('rides')

def deleteride(request):
    if not request.GET['id']:
        return HttpResponse("No ID")
    
    DriveRequest.objects.filter(ID=request.GET['id']).delete()
    return redirect('rides')


#  def showRides(request):
#     return render(request,'showRides.html');