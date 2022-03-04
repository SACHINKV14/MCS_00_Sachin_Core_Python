
from django.shortcuts import render,HttpResponse

# Create your views here.
dict1={}
def home(request):
    teams=["RCB","MI","CSK","DC","PBSK","KKR","RR","SRH","LSG","GT"]
    if request.method=="POST":
        vote1=request.POST.get("id1")
        if vote1 not in dict1:
            dict1[vote1] =1
        else:
            dict1[vote1] += 1
        dict2=dict(sorted(dict1.items(),key=lambda x:x[1],reverse=True))
        # print(dict2)
        context = {'iplteam': []}

        for key,value in dict2.items():
            dict3 = {}
            dict3['team_name']=key
            dict3['team_score']=value
            context['iplteam'].append(dict3)

        # print("context",context)
        return render(request, "index.html",context=context)




    return render(request,"index.html")

