from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.shortcuts import render,redirect
from accounts.forms import RegistrationForm, ProfileRegistrationForm
from django.http import Http404
from django.contrib.auth import logout as customLogout
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.http import HttpResponse

def index(request):
    formRegister = RegistrationForm()
    formLogin = AuthenticationForm()
    
    if request.user.is_authenticated:
        return render(request, 'login.html')

    if request.method == 'POST':
        print("Hello")
        formRegister = RegistrationForm(request.POST)
        print("user instance = ")
        print(formRegister.instance)
        formProfileRegister = ProfileRegistrationForm(request.POST)
        print("profile instance = ")
        print(formProfileRegister.instance)
        formLogin = AuthenticationForm(data=request.POST)
        
        if not formRegister.is_valid():
            print("formRegister not valid")
            print(formRegister.errors)
                    
        if not formProfileRegister.is_valid():
            print("formProfileRegister not valid")
            print(formProfileRegister.errors)
		
        if formRegister.is_valid() and formProfileRegister.is_valid():
            formRegister.save() #this creates user and profile
            formProfileRegister.instance.pk = formRegister.instance.profile.pk
            formProfileRegister.instance.user = formRegister.instance
            formProfileRegister.save()
            username = formRegister.cleaned_data.get("username")
            password1 = formRegister.cleaned_data.get("password1")
            print(username)
            print(password1)
            user = authenticate(username=username, password=password1)
            print(user)
            login(request,user)
            return redirect('regsuccess')

        if formLogin.is_valid():
            print("IN")
            username = formLogin.cleaned_data.get("username")
            password1 = formLogin.cleaned_data.get("password")
            print(username)
            print(password1)
            user = authenticate(request, username=username, password=password1)
            if request.POST['remember_me']:
                request.session.set_expiry(1209600)
            context = {'form': formLogin}
            if user:
                print("Not none")
                login(request,user)
                return render(request, 'login.html', context)
        else:
            return HttpResponse(formRegister.errors + formProfileRegister.errors)
            
    else:
        formRegister = RegistrationForm()
        formProfileRegister = ProfileRegistrationForm(request.POST)
        return render(request,'homePage.html', {'formRegister':formRegister,'formLogin':formLogin, 'formProfileRegister':formProfileRegister})




def loginpage(request):
    return render(request,'login.html')

def registerPage(request):
    return render(request,'register.html')

def driverpage(request):
    return render(request,'driver_page.html')
def regsuccess(request):
    return render(request,'regSuccess.html')
def logout(request):
    print(request)
    customLogout(request)
    return redirect('index')
def ridepopup(request):
    return render(request, 'ridePopup.html')

