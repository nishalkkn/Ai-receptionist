from django.http import HttpResponseRedirect
from django.shortcuts import render
from login.models import Login

# Create your views here.
def login(request):
    if request.method == "POST":
        uname = request.POST.get("un")
        passw = request.POST.get("ps")
        obj = Login.objects.filter(user_name=uname,password=passw)
        tp =""
        for ob in obj :
            tp =ob.type
            uid=ob.uid
            if tp == "admin":
                request.session["uid"] = uid
                return HttpResponseRedirect('/temp/admin/')
            elif tp == "user":
                request.session["uid"] = uid
                return HttpResponseRedirect('/temp/user/')
            elif tp == "doctor":
                request.session["uid"] = uid
                return HttpResponseRedirect('/temp/doctor/')
        else:
            objlist = "Username or password incorrect... please try angin...!"
            context = {
                'msg': objlist,
                }
            return  render(request, 'login/login.html', context)
    return render(request,'login/login.html')