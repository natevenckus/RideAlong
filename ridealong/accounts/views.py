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
from django.core.mail import send_mail

def index(request):
    formRegister = RegistrationForm()
    formLogin = AuthenticationForm()
    num = request.session.get_expiry_age()
    print(request.POST)
    print("Expiry age")
    print(num)
    if request.user.is_authenticated and num is not 0:
        return render(request, 'login.html') 

    if request.method == 'POST':
       
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
            
            user = authenticate(username=username, password=password1)
            email1 = send_mail('Ridealong Registration','Congratulations for Registering with RideAlong. Here is your confirmation email',to=[user.email])
            email1.send()
            login(request,user)
            return redirect('regsuccess')

        if formLogin.is_valid():
            print("IN")
            username = formLogin.cleaned_data.get("username")
            password1 = formLogin.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password1)
			
            print(request.POST)
            
            if "remember_me" in request.POST.keys() and request.POST['remember_me']:
                request.session.set_expiry(45)
                print(request.session.get_expiry_age())
            else:
                request.session.flush()
                request.session.set_expiry(0)
                print("DO NOT REMEMBER ME")
                print(request.session.get_expiry_age())

            context = {'form': formLogin}
            if user:
                print("Not none")
                login(request,user)
                return render(request, 'login.html', context)
            
    else:
        formRegister = RegistrationForm()
        formProfileRegister = ProfileRegistrationForm(request.POST)
        return render(request,'homePage.html', {'formRegister':formRegister,'formLogin':formLogin, 'formProfileRegister':formProfileRegister})
        
    return render(request,'homePage.html', {'formRegister':formRegister,'formLogin':formLogin })

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

def forgotpass(request):
    return render(request, 'forgot-pass.html')
def resetpass(request):
    return render (request, 'request-pass.html')
    
