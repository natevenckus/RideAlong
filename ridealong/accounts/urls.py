from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('registerpage',views.loginpage, name='registerpage'),
    path('loginpage',views.loginpage, name='loginpage'),
    path('driverpage',views.driverpage,name='driverpage'),
    path('regsuccess', views.regsuccess, name='regsuccess'),
    path('logout',views.logout, name='logout'),
    path('ridepopup', views.ridepopup, name='ridepopup'),
    path('forgotpass', views.forgotpass, name='forgotpass'),
    path('resetpass', views.resetpass, name="resetpass")
    
    #path('login',views.loginPage),
    #path('register',views.registerPage),
    #path(r'^login/$',views.loggedIn,name='loggedIn'),
    #path('register',views.register,name="register"),

]
