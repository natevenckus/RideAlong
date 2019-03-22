from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
    if not request.user.is_authenticated:
        return redirect('loginpage')
    
    return render(request,'rider_page.html')
