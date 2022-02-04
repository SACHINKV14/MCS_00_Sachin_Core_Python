from django.contrib import admin
from .models import Credential,Courses,Admins


# Register your models here.
admin.site.register(Credential)
admin.site.register(Courses)
admin.site.register(Admins)

