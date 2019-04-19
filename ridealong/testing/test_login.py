from django.test import TestCase
from django.test import Client
from ridealong.accounts import views

class Testcases(TestCase):
    def loginTestCase: 
        print("in loginTestCase")
        c = Client()
        response = c.post('/login/', {'username': 'sougz7', 'password': 'ridealong678', 'remember_me': 'true', 'login': 'Login'})
        if response.status_code == 200:
            print("passed loginTestCase")
            return True
        