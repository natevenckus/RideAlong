from django.db import models
from django.contrib.auth.models import User
from driver.models import RiderLink
from django.db.models.signals import post_save
from django.dispatch import receiver

#Design based on https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	FBID = models.CharField(max_length=50, null=True, blank=True)
	FullName = models.CharField(max_length=100, null=True, blank=True)
	SchoolEmail = models.EmailField(null=True, blank=True)
	ContactEmail = models.EmailField(null=True, blank=True)
	PhoneNum = models.CharField(max_length = 20, null=True, blank=True)
	Gender = models.CharField(max_length = 20, null=True, blank=True)
	DOB = models.DateField(null=True, blank=True)
	SchoolName = models.CharField(max_length=50, null=True, blank=True)
	ProfilePic = models.BinaryField(null=True, blank=True)
	EduVerified = models.BooleanField(default=False, null=True, blank=True)
	EduVerifyTime = models.DateTimeField(null=True, blank=True)

class Review(models.Model):
    ID = models.AutoField(primary_key=True)
    Reviewer = models.ForeignKey(User, related_name="reviewer_user", on_delete=models.CASCADE, blank=True,null=True)
    Reviewee = models.ForeignKey(User, related_name="reviewee_user", on_delete=models.CASCADE, blank=True,null=True)
    Ride = models.ForeignKey("driver.RiderLink", on_delete=models.CASCADE, blank=True,null=True)
    Rating = models.DecimalField(decimal_places=1, max_digits = 2, blank=True, null=True)
    Title = models.CharField(max_length=100)
    ReviewText = models.CharField(max_length = 500)
    Anon = models.BooleanField(blank=True, null=True)
    ReviewTime = models.DateTimeField(blank=True, null=True)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created: #means new record was created in database
        print("Creating user profile")
        Profile.objects.create(user=instance) #Creates profile object w user field set to caller
        print("Its id is ")
        print(Profile.objects.get(user=instance).pk)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print("Save user profile")
    instance.profile.save()
