from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Credential,Courses

# Create your views here.
def login(request):

    if request.method=="POST":
        pnum=request.POST.get("pnumber")    #take name in html
        pword=request.POST.get("pword")
        login = request.POST.get("login")
        user1 = Credential.objects.filter(phonenumber=pnum,password=pword).first()
        upword=user1.password
        print("upword",upword,'\t',"pword",pword)

        upnum=user1.phonenumber
        print("upnum",upnum,'\t',"pnum",pnum)
        if login:
            if pnum==upnum and pword==upword:
                return redirect("course")

            else:
                context1={"val1":"please check phone number and password"}
                return render(request, "home1.html",context=context1)
    return render(request,"home1.html")


def index(request):
    if request.method=="POST":
        fn=request.POST.get("firstname")    #take name in html
        sn=request.POST.get("secondname")
        pn=request.POST.get("phonenumber")
        un=request.POST.get("username")
        pw=request.POST.get("password")
        cpw=request.POST.get("cpassword")

        register=request.POST.get("register")

        #to check phone number exists in user
        user=Credential.objects.filter(phonenumber=pn).first()
        if user==None:
            a=0
        else:
            a=user.phonenumber
        if a!=pn or user==None:
            if register:
                if pw==cpw:
                    context ={"val": "succeful"}
                    new_user=Credential(firstname=fn,secondname=sn,username=un,phonenumber=pn,password=pw)
                    new_user.save()
                    # return render(request,"home.html", context=context)
                    return redirect("login")


                else:
                    context={"val":"password din't match"}
                    return render(request,"home.html",context=context)
        elif a==pn:
            context = {"val": "user already exist with the Phone number "}
            return render(request, "home.html", context=context)



    return render(request,"home.html")


def course(request):
    coursedetails=Courses.objects.all()
    print(coursedetails)
    return render(request,"course.html",{"context":coursedetails})


def courseupdate(request):
    return render(request,"courseupdate.html")