from django.urls import path
from firstproject.helloworld.migrations import views

urlpatterns=[
    path('',views.index,name='index')
]

