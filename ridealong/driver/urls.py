from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='driverpage'),
    path('search',views.driverSearch,name='driversearch'),
    path('ridepopup',views.ridepopup,name='ridepopup'),
    path('profile', views.profile, name = 'profile'),
    path('saveprofile', views.saveprofile, name='saveprofile'),
    #path('rider', views.rider, name='rider'),
    #path('driver', views.driver, name='driver'),
    path('rides', views.rides, name='rides'),
]

