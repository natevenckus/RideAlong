from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import  UserCreationForm
from django.shortcuts import render,redirect


def index(request):
    formRegister = UserCreationForm()
    formLogin = UserCreationForm()

    return render(request,'homePage.html', {'formRegister':formRegister,'formLogin':formLogin })



#not needed
def loginPage(request):
    return render(request,'login.html')

def registerPage(request):
    return render(request,'register.html')

def register(request):
    form = UserCreationForm()

    return render(request,'homePage.html',{'form':form})
