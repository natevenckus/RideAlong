from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='riderpage'),
    path('ridepopup',views.ridepopup,name='ridepopup'),
    path('profile', views.profile, name = 'profile'),
]
