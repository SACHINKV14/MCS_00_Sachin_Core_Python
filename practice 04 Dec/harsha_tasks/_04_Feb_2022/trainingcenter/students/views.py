from django.shortcuts import render,HttpResponse,redirect
from .models import Credential,Courses,Admins
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method=="POST":
        a=request.POST.get("admin")
        b=request.POST.get("signin")
        c=request.POST.get("signup")
        if a:
            return redirect("adminf")
        elif b:
            return redirect("signinf")
        elif c:
            return redirect("signupf")

    return render(request,"home.html")

def adminf(request):
    if request.method=="POST":
        sdb=request.POST.get("studentdb")
        cdb=request.POST.get("coursedb")
        if sdb:
            return redirect("studentdbf")
        elif cdb:
            return redirect("coursedbf")

    return render(request,"adminpage.html")


def signinf(request):
    if request.method=="POST":
        pnums=request.POST.get("pnumber")    #take name in html
        pwords=request.POST.get("pword")
        logins = request.POST.get("login")
        user1s = Credential.objects.filter(phonenumber=pnums).first()
        upwords=user1s.password
        print("upword",upwords,'\t',"pword",pwords)

        upnum=user1s.phonenumber
        print("upnum",upnum,'\t',"pnum",pnums)
        if logins:
            if pnums==upnum and pwords==upwords:
                coursedetailsl = Courses.objects.all()
                return render(request,"allcoursesavailable.html",{"context":coursedetailsl})

            else:
                messages.info(request, "Check your Phone number & Password ")
                return render(request,"studentlogin.html")

    return render(request,"studentlogin.html")


def signupf(request):
    if request.method=="POST":
        fn=request.POST.get("firstname")    #take name in html
        sn=request.POST.get("secondname")
        pn=request.POST.get("phonenumber")
        un=request.POST.get("username")
        pw=request.POST.get("password")
        cpw=request.POST.get("cpassword")

        register=request.POST.get("registers")

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
                    return redirect("signinf")


                else:
                    context={"val":"password din't match"}
                    return render(request,"register.html",context=context)
        elif a==pn:
            context = {"val": "user already exist with the Phone number "}
            return render(request, "register.html", context=context)

    return render(request, "register.html")

def coursedbf(request):
    coursedetails = Courses.objects.all()

    if request.method == "POST":
        c_add = request.POST.get("courseadd")
        c_delete = request.POST.get("coursedelete")
        c_update = request.POST.get("courseupdate")
        if c_add:
            return redirect("courseaddf")

        elif c_delete:
            return redirect("coursedeletef")

        elif c_update:
            return redirect("courseupdatef")


    return render(request, "coursedb.html", {"context": coursedetails})

def studentdbf(request):
    studentdetails = Credential.objects.all()


    if request.method == "POST":
        s_add = request.POST.get("studentadd")
        s_delete = request.POST.get("studentdelete")
        s_update = request.POST.get("studentupdate")
        if s_add:
            return redirect("studentaddf")

        elif s_delete:
            return redirect("studentdeletef")

        elif s_update:
            return redirect("studentupdatef")

    return render(request, "studentdb.html", {"context": studentdetails})


def courseaddf(request):
    coursedetails = Courses.objects.all()
    if request.method == "POST":
        c_add_cn = request.POST.get("coursename")
        c_add_cf = request.POST.get("coursefees")
        c_add_ch = request.POST.get("coursehours")
        c_add_t = request.POST.get("trainer")
        c_add_add = request.POST.get("add")

        course = Courses.objects.filter(coursename=c_add_cn).first()
        if course == None:
            course_a = 0
        else:
            course_a = course.coursename

        if course_a != c_add_cn or course_a == 0:
            if c_add_add:
                context = {"val": "succeful"}
                new_course = Courses(coursename=c_add_cn,coursefees=c_add_cf,hours=c_add_ch,trainer=c_add_t)
                new_course.save()
                coursedetails1 = Courses.objects.all()
                return render(request,"courseadd.html", {"context": coursedetails1})

        elif course_a == c_add_cn:
            print("in c_add elif")
            context = {"val": "Course already exists "}
            return render(request,"courseadd.html", context=context)


    return render(request, "courseadd.html",{"context": coursedetails})

def coursedeletef(request):
    coursedetails_d = Courses.objects.all()
    if request.method=="POST":
        id1=request.POST.get("courseid")
        courseid=Courses.objects.get(id=id1)
        courseid.delete()
        return redirect("coursedeletef")

    return render(request,"coursedelete.html",{"context": coursedetails_d})

def courseupdatef(request):
    coursedetails_u = Courses.objects.all()
    if request.method=="POST":
        idu=request.POST.get("courseid")
        courseidu=Courses.objects.get(id=idu)
        courseidu.coursename = request.POST.get("coursename")
        courseidu.coursefees = request.POST.get("coursefees")
        courseidu.coursehours = request.POST.get("coursehours")
        courseidu.trainer = request.POST.get("trainer")
        course_u = request.POST.get("update")
        if course_u:
            courseidu.save()
        return redirect("courseupdatef")

    return render(request,"courseupdate.html",{"context": coursedetails_u})




def studentaddf(request):
    studentdetails_a = Credential.objects.all()
    print("-------------------------------------------------------")
    if request.method == "POST":
        fna = request.POST.get("firstnamea")  # take name in html
        sna = request.POST.get("secondnamea")
        pna = request.POST.get("phonenumbera")
        una = request.POST.get("usernamea")
        pwa = request.POST.get("passworda")

        registera = request.POST.get("addstudent")

        # to check phone number exists in user
        usera = Credential.objects.filter(phonenumber=pna).first()
        if usera == None:
            aa = 0
        else:
            aa = usera.phonenumber
        if aa != pna or usera == None:
            if registera:

                context = {"val": "succeful"}
                new_usera = Credential(firstname=fna, secondname=sna, username=una, phonenumber=pna, password=pwa)
                new_usera.save()
                return redirect("studentaddf")

        elif aa == pna:
            messages.info(request,"user already exist with the Phone number ")
            return redirect("studentaddf")

    print("-------------------------------------------------------")
    return render(request,"studentadd.html",{"context":studentdetails_a})


def studentdeletef(request):
    studentdetails_d = Credential.objects.all()
    if request.method == "POST":
        sid1 = request.POST.get("studentid")
        studentid = Credential.objects.get(id=sid1)
        studentid.delete()
        return redirect("studentdeletef")

    return render(request, "studentdelete.html", {"context": studentdetails_d})

def studentupdatef(request):
    studentdetails_u = Credential.objects.all()
    if request.method == "POST":
        sidu = request.POST.get("studentidu")
        studentidu = Credential.objects.get(id=sidu)

        studentidu.username = request.POST.get("usernameu")
        studentidu.firstname = request.POST.get("firstnameu")
        studentidu.secondname = request.POST.get("secondnameu")
        studentidu.phonenumber = request.POST.get("phonenumberu")
        studentidu.password = request.POST.get("passwordu")

        student_u = request.POST.get("update")
        if student_u:
            studentidu.save()
        return redirect("studentupdatef")

    return render(request, "studentupdate.html", {"context": studentdetails_u})


def adminsf(request):
    adminuser = Admins.objects.filter(adminusername=pna).first()
    if request.method == "POST":
        adminun=request.POST.get("adminusername")
        adminpw=request.POST.get("adminpassword")
    pass
