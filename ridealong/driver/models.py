from django.db import models
from django.contrib.auth.models import User

class DriveRequest(models.Model):
    ID = models.AutoField(primary_key=True)
    Rider = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    FromLat = models.DecimalField(decimal_places=10, max_digits=15,null=True)
    FromLong = models.DecimalField(decimal_places=10, max_digits=15,null=True)
    ToLat = models.DecimalField(decimal_places=10, max_digits=15,null=True)
    ToLong = models.DecimalField(decimal_places=10, max_digits=15,null=True)
    MinDepartTime = models.DateTimeField(null=True)
    MaxDepartTime = models.DateTimeField(null=True)
    PriceOffer = models.DecimalField(decimal_places=2, max_digits=10,null=True)
    LuggageSqFt = models.DecimalField(decimal_places=2, max_digits=5,null=True)
    RequestTime = models.DateTimeField(null=True)
    Completed = models.BooleanField(null=True)
    CompleteTime = models.DateTimeField(null=True)
    #additional columns
    #Driver = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    departLoc = models.CharField(default="departureLoc",max_length=100)
    arrivalLoc = models.CharField(default="arrivalLoc",max_length=100)
    pickupTime = models.DateTimeField()
    dropTime = models.DateTimeField()
    numOfSeats = models.IntegerField()
    numOfBaggage = models.IntegerField()



