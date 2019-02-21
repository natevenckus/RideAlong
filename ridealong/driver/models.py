from django.db import models
from django.contrib.auth.models import User

class DriveRequest(models.Model):
	ID = models.AutoField(primary_key=True)
	Rider = models.ForeignKey(User, on_delete=models.CASCADE)
	FromLat = models.DecimalField(decimal_places=10, max_digits=15)
	FromLong = models.DecimalField(decimal_places=10, max_digits=15)
	ToLat = models.DecimalField(decimal_places=10, max_digits=15)
	ToLong = models.DecimalField(decimal_places=10, max_digits=15)
	MinDepartTime = models.DateTimeField()
	MaxDepartTime = models.DateTimeField()
	PriceOffer = models.DecimalField(decimal_places=2, max_digits=10)
	LuggageSqFt = models.DecimalField(decimal_places=2, max_digits=5)
	RequestTime = models.DateTimeField()
	Completed = models.BooleanField()
	CompleteTime = models.DateTimeField()

# Create your models here.
