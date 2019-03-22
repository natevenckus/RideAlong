from django.shortcuts import render
from django.shortcuts import redirect
from .models import DriveRequest, Car
from accounts.models import Profile
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.db.models.functions import Cast
from django.db.models import CharField
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
            driveRequest_instance = DriveRequest.objects.create(
                departLoc = request.POST['departLoc'],
                arrivalLoc = request.POST['arrivalLoc'],
                pickupTime = request.POST['pickupTime'],
                dropTime = request.POST['dropTime'],
                numOfSeats = request.POST['seats'],
                numOfBaggage = request.POST['baggage'],
            )
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

    driveRequests = DriveRequest.objects.all()
    #times = DriveRequest.objects.all().values_list('pickupTime',flat=True)
    #print (times)
    print("driveRequests:")
    print(driveRequests)
    return render(request,"driver_page.html",{'isIndex':True,'driveRequests':driveRequests})

def driverSearch(request):
    #ex. query http://localhost:8000/driver/search?searchLocation=West&filter=location
    #ex. query for date http://localhost:8000/driver/search?searchYear=2222&searchMonth=2&searchDay=2&filter=date
    #filter options: location,date,price,luggage,passengershttp://localhost:8000/driver/search?Filter=Price
    if request.method == "GET":
        print (request.GET)
        if request.GET['filter'] == 'location':
            searchResult = DriveRequest.objects.filter(departLoc__search=request.GET['searchLocation'])
        elif request.GET['filter'] == 'date':
            searchResult = DriveRequest.objects.filter(pickupTime__year=request.GET['searchYear'], pickupTime__month=request.GET['searchMonth'],pickupTime__day=request.GET['searchDay'])
        elif request.GET['filter'] == 'price':
            q = SearchQuery(request.GET['searchPrice'])
            vector = SearchVector(Cast('PriceOffer', CharField()))
            searchResult=DriveRequest.objects.annotate(search=vector).filter(search=q)
        elif request.GET['filter'] == 'luggage':
            q = SearchQuery(request.GET['searchLuggage'])
            vector = SearchVector(Cast('numOfBaggage', CharField()))
            searchResult=DriveRequest.objects.annotate(search=vector).filter(search=q)
        elif request.GET['filter'] == 'passenger':
            q = SearchQuery(request.GET['searchPassenger'])
            vector = SearchVector(Cast('numOfSeats', CharField()))
            searchResult=DriveRequest.objects.annotate(search=vector).filter(search=q)

    return render(request,"driver_page.html",{'isIndex':False,'searchResult':searchResult})

def ridepopup(request):
    return render(request,'ridePopup.html')

def profile(request):
    if request.user.is_authenticated:
        print("IN")
        username = request.user.email
        #print(userName)
        profilePage = Profile.objects.filter(ContactEmail=username)
        return render(request,"profile.html",{'profilePage':profilePage})
    else:
        return render(request, "profile.html")
    # return render(request, 'profile.html')

