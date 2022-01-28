from django.db import models

# Create your models here.

class Alarm(models.Model):
    HH=models.IntegerField(null=False)
    MM=models.IntegerField(null=False)



