from django.shortcuts import render
from django.http import HttpResponse
from django.test import TestCase
from django.test import Client
from accounts import views
import requests
 
def index(request):
    
    print("in loginTestCase")
    c = Client()
    return HttpResponse("testing webpage")
    r = requests.post(url='localhost:8000/', data={'username': 'sougz7', 'password': 'ridealong678', 'remember_me': 'true', 'login': 'Login'})
    print ("response status code")
    print(r.status_code)
    if r.status_code == 200:
        print("passed loginTestCase")
        return HttpResponse("passed loginTestCase")
    else:
        print("failed loginTestCase")
        return HttpResponse("failed loginTestCase")
    