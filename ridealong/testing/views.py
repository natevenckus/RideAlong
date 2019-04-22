from django.shortcuts import render
from django.http import HttpResponse
from django.test import TestCase
from django.test import Client
from accounts import views
 
def index(request):
    
    print("in loginTestCase")
    c = Client()
    response = c.post('', {'username': 'sougz7', 'password': 'ridealong678', 'remember_me': 'true', 'login': 'Login'})
    print (response.status_code)
    if response.status_code == 400:
        print("passed loginTestCase")
        return HttpResponse("passed loginTestCase")
    else:
        print("failed loginTestCase")
        return HttpResponse("failed loginTestCase")
    return HttpResponse("testing page")