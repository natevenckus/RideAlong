from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='riderpage'),
    path('rides1', views.rides1, name='rides1'),
    path('search',views.riderSearch,name='ridersearch'),
    path('deleteride', views.deleteride, name='deleteride'),
    path('updateride', views.updateride, name='updateride'),
    #path('rider', views.rider, name='rider'),
    #path('driver', views.driver, name='driver')
]
