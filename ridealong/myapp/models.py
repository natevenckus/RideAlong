from django.db import models

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

