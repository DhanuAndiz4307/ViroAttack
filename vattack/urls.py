from django.urls import path

from . import views

urlpatterns=[
    path('',views.Userlogin,name='Userlogin'),
    path('signup/',views.signup,name='signup'),
    path('survey/',views.survey,name='survey'),
    path('homepage/',views.homepage,name='homepage'),
    path('tracking/',views.tracking,name='tracking'),
    path('about/',views.about,name='about'),
    path('logout/',views.logout,name='logout') 
           ]