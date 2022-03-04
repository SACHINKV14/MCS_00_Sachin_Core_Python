from django.shortcuts import render,redirect
# Create your views here.
def home(request):
    if request.method=="POST":
        cal=request.POST.get("cal")
        exp = request.POST.get("result")
        if cal and exp==None:
            return redirect("home")
        try:
            result=eval(exp)
            print(result)
        except Exception as e:
            return render(request,"index.html",{"context":'invalid expression'})
        return render(request,"index.html",{"context":result})
    return render(request,"index.html")