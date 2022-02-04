from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adminf/',views.adminf,name='adminf'),
    path('signinf/',views.signinf,name='signinf'),
    path('signupf/',views.signupf,name='signupf'),
    path('studentdbf/',views.studentdbf,name='studentdbf'),
    path('coursedbf/',views.coursedbf,name='coursedbf'),

    path('courseaddf/', views.courseaddf, name='courseaddf'),
    path('coursedeletef/', views.coursedeletef, name='coursedeletef'),
    path('courseupdatef/', views.courseupdatef, name='courseupdatef'),

    path('studentaddf/', views.studentaddf, name='studentaddf'),
    path('studentdeletef/', views.studentdeletef, name='studentdeletef'),
    path('studentupdatef/', views.studentupdatef, name='studentupdatef'),

    path('adminsf/',views.adminsf,name='adminsf')


]