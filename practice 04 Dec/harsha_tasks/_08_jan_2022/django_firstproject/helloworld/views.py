from django.shortcuts import render
#imports
from django.http import HttpResponse

#hardcoded
# def index(request):
#     return HttpResponse("Hello world,You're at home") #directly giving output

#adding tempaltes directory
TEMPLATE_DIRS = (
    #joining this file folder and the temaplates folder
    'os.path.join(BASE_DIR,"templates"),'
)

#index html
# def index(request):
#     return render(request,"index.html")

#passing arguments to the templates
#passing datetime
import datetime
def index(request):
    today = datetime.datetime.now().date()
    return render(request,"index1.html",{"today":today})



# Create your views here.
