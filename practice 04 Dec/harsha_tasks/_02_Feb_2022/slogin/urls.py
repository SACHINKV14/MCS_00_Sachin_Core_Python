from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.login,name='login'),
    path('course',views.course,name='course'),
    path('courselogin/',views.course,name='course'),
    path('courseupdate',views.courseupdate,name='courseupdate'),

]

