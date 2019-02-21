from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#Design based on https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	FBID = models.CharField(max_length=50)
	FullName = models.CharField(max_length=100)
	SchoolEmail = models.EmailField()
	ContactEmail = models.EmailField()
	PhoneNum = models.CharField(max_length = 20)
	Gender = models.CharField(max_length = 20)
	DOB = models.DateField()
	CreationTime = models.DateTimeField()
	SchoolName = models.CharField(max_length=50)
	Car = models.ForeignKey("Car", on_delete=models.CASCADE)
	ProfilePic = models.BinaryField()
	EduVerified = models.BooleanField()
	EduVerifyTime = models.DateTimeField()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
	
class Car(models.Model):
	ID = models.AutoField(primary_key=True)
	Make = models.CharField(max_length=30)
	Model = models.CharField(max_length=30)
	Year = models.IntegerField()
