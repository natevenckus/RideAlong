from django.db import models
from django.contrib.auth.models import User

class RideRequest(models.Model):
    ID = models.AutoField(primary_key=True)
    Rider = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True)
    FromLat = models.DecimalField(decimal_places=10, max_digits=15,blank=True,null=True)
    FromLong = models.DecimalField(decimal_places=10, max_digits=15,blank=True,null=True)
    ToLat = models.DecimalField(decimal_places=10, max_digits=15,blank=True,null=True)
    ToLong = models.DecimalField(decimal_places=10, max_digits=15,blank=True,null=True)
    MinDepartTime = models.DateTimeField(blank=True,null=True)
    MaxDepartTime = models.DateTimeField(blank=True,null=True)
    PriceOffer = models.DecimalField(decimal_places=2, max_digits=10,blank=True,null=True)
    LuggageSqFt = models.DecimalField(decimal_places=2, max_digits=5,blank=True,null=True)
    RequestTime = models.DateTimeField(blank=True,null=True)
    Completed = models.BooleanField(blank=True,null=True)
    CompleteTime = models.DateTimeField(blank=True,null=True)
    departLoc = models.CharField(default="departureLoc",max_length=100)
    arrivalLoc = models.CharField(default="arrivalLoc",max_length=100)
    pickupTime = models.DateTimeField()
    dropTime = models.DateTimeField()
    seatsNeeded = models.IntegerField()
    baggageNeeded = models.IntegerField()
