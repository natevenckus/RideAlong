from django.db import models

#Put models here
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class User(models.Model):
	ID = models.AutoField(primary_key=True)
	FBID = models.CharField(max_length=50)
	FullName = models.CharField(max_length=100)
	SchoolEmail = models.EmailField()
	ContactEmail = models.EmailField()
	PhoneNum = models.CharField(max_length = 20)
	Gender = models.CharField(max_length = 20)
	DOB = models.DateField()
	CreationTime = models.DateTimeField()
	SchoolName = models.CharField(max_length=50)
	CarMake = models.CharField(max_length=30)
	CarModel = models.CharField(max_length=30)
	CarYear = models.IntegerField()
	ProfilePic = models.BinaryField()
	EduVerified = models.BooleanField()
	EduVerifyTime = models.DateTimeField()

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

class Profile(models.Model):
	user = models.OneToOnField(User,on_delete = models.CASCADE)
	email_confirmation = models.BooleanField(default=False)

#@receiver(post_save, sender=User)
#def update_user_profile(sender,instance,created,**kwargs):
#	if created:
#		Profile.objects.create(user=instance)
#	instance.profile.save()
