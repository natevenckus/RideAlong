from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVectorField
from datetime import datetime

class DriveRequest(models.Model):
    ID = models.AutoField(primary_key=True)
    Rider = models.ForeignKey(User, on_delete=models.CASCADE, blank=False,null=False)
    FromLat = models.DecimalField(decimal_places=10, max_digits=15,blank=True,null=True)
    FromLong = models.DecimalField(decimal_places=10, max_digits=15,blank=True,null=True)
    ToLat = models.DecimalField(decimal_places=10, max_digits=15,blank=True,null=True)
    ToLong = models.DecimalField(decimal_places=10, max_digits=15,blank=True,null=True)
    MinDepartTime = models.DateTimeField(blank=True,null=True)
    MaxDepartTime = models.DateTimeField(blank=True,null=True)
    PriceOffer = models.DecimalField(decimal_places=2, max_digits=10,blank=True,null=True)
    LuggageSqFt = models.DecimalField(decimal_places=2, max_digits=5,blank=True,null=True)
    RequestTime = models.DateTimeField(default=datetime.now,blank=True,null=True)
    Completed = models.BooleanField(blank=True,null=True)
    CompleteTime = models.DateTimeField(blank=True,null=True)
    #additional columns
    #Driver = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    departLoc = models.CharField(default="departureLoc",max_length=100)
    arrivalLoc = models.CharField(default="arrivalLoc",max_length=100)
    pickupTime = models.DateTimeField()
    dropTime = models.DateTimeField()
    numOfSeats = models.IntegerField()
    numOfBaggage = models.IntegerField()
    Car = models.ForeignKey("Car", on_delete=models.CASCADE, null=True, blank=True)

class Car(models.Model):
    ID = models.AutoField(primary_key=True)
    Make = models.CharField(max_length=30)
    Model = models.CharField(max_length=30)
    Year = models.IntegerField()

class Review(models.Model):
    ID = models.AutoField(primary_key=True)
    Reviewer = models.ForeignKey(User, related_name="reviewer_user", on_delete=models.CASCADE, blank=True,null=True)
    Reviewee = models.ForeignKey(User, related_name="reviewee_user", on_delete=models.CASCADE, blank=True,null=True)
    Ride = models.ForeignKey("RiderLink", on_delete=models.CASCADE, blank=True,null=True)
    Rating = models.DecimalField(decimal_places=1, max_digits = 2, blank=True, null=True)
    Title = models.CharField(max_length=100)
    ReviewText = models.CharField(max_length = 500)
    Anon = models.BooleanField(blank=True, null=True)
    ReviewTime = models.DateTimeField(blank=True, null=True)

class RiderLink(models.Model):
    ID = models.AutoField(primary_key=True)
    Rider = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True)
    DriveRequest = models.ForeignKey(DriveRequest, on_delete=models.CASCADE, blank=True,null=True)
    Confirmed = models.BooleanField(default=False, blank=True, null=True)
    ConfirmedTime = models.DateTimeField(blank=True, null=True)
    Denied = models.BooleanField(default=False, blank=True, null=True)
    DeniedTime = models.DateTimeField(blank=True, null=True)