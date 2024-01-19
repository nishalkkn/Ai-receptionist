from django.http import HttpResponseRedirect
from django.shortcuts import render
from service.models import Service
from department.models import Department

# Create your views here.
def service(request):
    obj=Department.objects.all()
    context={
        'x':obj
    }
    if request.method=='POST':
        obj=Service()
        obj.name=request.POST.get('ps')
        obj.dept_id=request.POST.get('dept')
        obj.save()
        return HttpResponseRedirect('/service/viewser/')
    return render(request,'service/service.html',context)


def vser(request):
    obj = Service.objects.all()
    context = {
        'x': obj
    }
    return render(request,'service/view_service.html',context)


def remove(request,idd):
    obb=Service.objects.get(service_id=idd)
    obb.delete()
    return vser(request)