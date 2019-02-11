from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pwtest(request):
   #return render(request, "myapp/template/pwtest.html", {})
   return HttpResponse("Password test (updated)")