from django.http import HttpResponseRedirect
from django.shortcuts import render
from complaint.models import Complaint
import datetime
from user.models import User
# Create your views here.
def complaint(request):
    ss=request.session["uid"]
    if request.method=='POST':
        obj=Complaint()
        obj.user_id=ss
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.complaint=request.POST.get('complaint')
        obj.save()
        return HttpResponseRedirect('/temp/user/')
    return render(request,'complaint/complaint.html')


def vcom(request):

    obj = Complaint.objects.all()
    context = {
        'x': obj
    }
    return render(request,'complaint/view_complaint.html',context)


def reply(request,idd):
    if request.method=='POST':
        obj=Complaint.objects.get(comp_id=idd)
        obj.replay=request.POST.get('un')
        obj.save()
        return vcom(request)
    return render(request,'complaint/reply.html')

def vre(request):
    ss=request.session["uid"]
    obj=Complaint.objects.filter(user_id=ss)
    context={
        'x':obj
    }
    return render(request,'complaint/view_reply.html',context)
