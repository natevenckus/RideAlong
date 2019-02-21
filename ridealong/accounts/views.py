from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.shortcuts import render,redirect
from accounts.forms import RegistrationForm
from django.http import Http404
from django.contrib.auth import logout as customLogout
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from account.tokens import account_activation_token

def index(request):
    formRegister = RegistrationForm()
    formLogin = AuthenticationForm()
    
    if request.user.is_authenticated:
        return render(request, 'login.html')

    if request.method == 'POST':
        print("Hello")
        formRegister = RegistrationForm(request.POST)
        formLogin = AuthenticationForm(data=request.POST)
        
        if formRegister.is_valid():
            #my changes start here
            user = formRegister.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate your RideAlong Account FAAAAM'
            message = render_to_string('account_activation_email.html', {
                'user' : user,
                'domain': current_site.domain,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject,message)
            return redirect('regsuccess')

       

            #username = formRegister.cleaned_data.get("username")
            #password1 = formRegister.cleaned_data.get("password1")
            #print(username)
            #print(password1)
            #user = authenticate(username=username, password=password1)
            #print(user)
            #login(request,user)
            #return redirect('regsuccess')

        if formLogin.is_valid():
            print("IN")
            username = formLogin.cleaned_data.get("username")
            password1 = formLogin.cleaned_data.get("password")
            print(username)
            print(password1)
            user = authenticate(request, username=username, password=password1)
            if request.POST['remember_me'] == True:
                request.session.set_expiry(1209600)
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
def ridepopup(request):
    return render(request, 'ridePopup.html')

