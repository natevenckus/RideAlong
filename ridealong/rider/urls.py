from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='riderpage'),
    path('rides', views.rides, name='rides'),
    path('deleteride', views.deleteride, name='deleteride'),
    path('updateride', views.updateride, name='updateride'),
]