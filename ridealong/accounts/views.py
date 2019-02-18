from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.shortcuts import render,redirect
from accounts.forms import RegistrationForm
from django.http import Http404


def index(request):
    #formRegister = RegistrationForm()
    formLogin = AuthenticationForm()
    if request.method == 'POST':
        print("Hello")
        formRegister = RegistrationForm(request.POST)
        print(request.POST['username'])
        print(request.POST['password1'])
        print (request)
        if formRegister.is_valid():
            formRegister.save()
            username = formRegister.cleaned_data.get("username")
            password1 = formRegister.cleaned_data.get("password1")
            print(username)
            print(password1)
            user = authenticate(username=username, password=password1)
            #login(request,user)
            return redirect('loginpage')
        else: 
            print(formRegister.errors)
            raise Http404
    else:
        formRegister = RegistrationForm()
    return render(request,'homePage.html', {'formRegister':formRegister,'formLogin':formLogin })



#not needed
def loginpage(request):
    return render(request,'login.html')

def registerPage(request):
    return render(request,'register.html')


