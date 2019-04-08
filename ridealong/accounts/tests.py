from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import Profile



# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username = 'testuser')
        user.set_password('hello12345')
        user.save()
        user2 = User.objects.create(username = 'test2user')
        user2.set_password('hihowareu12345')
        user2.save()
        user3 = User.objects.create(username = 'test3user')
        user3.save()
        #c = Client()
        #logged_in = c.login(username = 'testuser',password = 'hello12345') 
        Profile.objects.create(user,FullName = 'testFullName',SchoolEmail = 'test@gmail.edu', ContactEmail = 'test@gmail.com', PhoneNum = '5622773131',Gender = 'Male', DOB = '07/30/1999', SchoolName = 'Purdue')
        Profile.objects.create(user2,FullName = 'testFullName2',SchoolEmail = 'test2@gmail.edu', ContactEmail = 'test2@gmail.com', PhoneNum = '5622773131',Gender = 'Male', DOB = '07/30/1999', SchoolName = 'Purdue')
        Profile.objects.create(user3,FullName = 'testFullName3',SchoolEmail = 'test3@gmail.edu', ContactEmail = 'test3@gmail.com', PhoneNum = '5622773131',Gender = 'Male', DOB = '07/30/1999', SchoolName = 'Purdue')

   # def test_login(self):


