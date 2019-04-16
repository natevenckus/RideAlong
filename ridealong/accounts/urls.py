from django.urls import path, include, re_path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import SetPasswordForm

urlpatterns=[
    path('',views.index,name='index'),
    path('registerpage',views.loginpage, name='registerpage'),
    path('loginpage',views.loginpage, name='loginpage'),
    path('regsuccess', views.regsuccess, name='regsuccess'),
    path('logout',views.logout, name='logout'),
    path('ridepopup', views.ridepopup, name='ridepopup'),
    path('forgotpass', views.forgotpass, name='forgotpass'),
    path('resetpass', views.resetpass, name="resetpass"),
    path('notifications', views.notfications,name='notifications'),
    path('accounts/password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #path('login',views.loginPage),
    #path('register',views.registerPage),
    #path(r'^login/$',views.loggedIn,name='loggedIn'),
    #path('register',views.register,name="register"),

]
