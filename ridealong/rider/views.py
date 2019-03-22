from django.shortcuts import render
from django.shortcuts import redirect

def riderpage(request):
    return render(request,'rider_page.html')

# Create your views here.
