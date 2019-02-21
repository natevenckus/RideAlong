from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('registerpage',views.loginpage, name='registerpage'),
    path('loginpage',views.loginpage, name='loginpage'),
    path('driverpage',views.driverpage,name='driverpage'),
    path('regsuccess', views.regsuccess, name='regsuccess'),
    path('logout',views.logout, name='logout'),
    path('ridepopup', views.ridepopup, name='ri
    #my changes
    url(r'^account_activation_sent/$',view.account_activation_sent, name = 'account_activation_sent'),
    

    #path('login',views.loginPage),
    #path('register',views.registerPage),
    #path(r'^login/$',views.loggedIn,name='loggedIn'),
    #path('register',views.register,name="register"),

]
