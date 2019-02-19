from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.shortcuts import render,redirect
from accounts.forms import RegistrationForm
from django.http import Http404
from django.contrib.auth import logout as customLogout


def index(request):
    formRegister = RegistrationForm()
    formLogin = AuthenticationForm()
    if request.method == 'POST':
        print("Hello")
        formRegister = RegistrationForm(request.POST)
        formLogin = AuthenticationForm(data=request.POST)
        
        if formRegister.is_valid():
            formRegister.save()
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
            context = {'form': formLogin}
            if user:
                print("Not none")
                login(request,user)
                return render(request, 'login.html', context)
        else:
            print(formLogin.errors)
            
    else:
        formRegister = RegistrationForm()
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


