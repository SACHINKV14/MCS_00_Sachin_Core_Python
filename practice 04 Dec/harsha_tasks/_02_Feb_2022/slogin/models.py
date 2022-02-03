from django.db import models

# Create your models here.
class Credential(models.Model):

    firstname=models.CharField(max_length=30)
    secondname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    phonenumber=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

class Courses(models.Model):
    coursename=models.CharField(max_length=30)
    coursefees=models.IntegerField(max_length=30)
    trainer=models.CharField(max_length=30)
    hours=models.IntegerField(max_length=30)

