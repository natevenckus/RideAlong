from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('registerpage',views.loginpage, name='registerpage'),
    path('loginpage',views.loginpage, name='loginpage'),
    path('regsuccess', views.regsuccess, name='regsuccess')

    #path('login',views.loginPage),
    #path('register',views.registerPage),
    #path(r'^login/$',views.loggedIn,name='loggedIn'),
    # path('register',views.register,name="register"),

]
