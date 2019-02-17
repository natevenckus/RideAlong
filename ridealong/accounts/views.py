from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.shortcuts import render,redirect
from accounts.forms import RegistrationForm


def index(request):
    formRegister = RegistrationForm()
    formLogin = AuthenticationForm()

    return render(request,'homePage.html', {'formRegister':formRegister,'formLogin':formLogin })



#not needed
def loginpage(request):
    return render(request,'login.html')

def registerPage(request):
    return render(request,'register.html')

def register(request):
    form = UserCreationForm()
    return render(request,'homePage.html',{'form':form})
