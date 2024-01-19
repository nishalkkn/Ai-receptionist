from django.http import HttpResponseRedirect
from django.shortcuts import render
from user.models import User
from login.models import Login

# Create your views here.
def user(request):
    if request.method=='POST':
        obj=User()
        obj.name=request.POST.get('name')
        obj.age=request.POST.get('age')
        obj.gender=request.POST.get('gender')
        obj.address=request.POST.get('address')
        obj.e_mail=request.POST.get('email')
        obj.phone_no=request.POST.get('phone')
        obj.password = request.POST.get('password')
        obj.save()

        ob = Login()
        ob.user_name = obj.name
        ob.password = obj.password
        ob.type = 'user'
        ob.uid = obj.user_id
        ob.save()
        return HttpResponseRedirect('/login/login')
    return render(request,'user/user.html')


def vuser(request):
    obj = User.objects.all()
    context = {
        'x': obj
    }
    return render(request,'user/view_user.html',context)