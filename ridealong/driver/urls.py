from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='driverpage'),
    path('search',views.driverSearch,name='driversearch'),
    path('ridepopup',views.ridepopup,name='ridepopup'),
    path('saveprofile', views.saveprofile, name='saveprofile'),
    path('drivernotifications',views.drivernotfications,name = 'drivernotifications'),
    path('updateride', views.updateride, name='updateride'),
    path('deleteride', views.deleteride, name='deleteride'),
    #path('rider', views.rider, name='rider'),
    #path('driver', views.driver, name='driver'),
    path('rides', views.rides, name='rides'),
]

