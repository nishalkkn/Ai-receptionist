from django.http import HttpResponseRedirect
from django.shortcuts import render
from department.models import Department

# Create your views here.
def department(request):
    if request.method=='POST':
        obj=Department()
        obj.dept_name=request.POST.get('ln')
        obj.save()
        return HttpResponseRedirect('/department/viewmgdept/')
    return render(request,'department/department.html')


def vdept(request):
    obj = Department.objects.all()
    context = {
        'x': obj
    }
    return render(request,'department/view_department.html',context)


def vmgdept(request):
    obj = Department.objects.all()
    context = {
        'x': obj
    }
    return render(request,'department/view_managedepaertment.html',context)

def remove(request,idd):
    obj=Department.objects.get(dept_id=idd)
    obj.delete()
    return vmgdept(request)

def reject(request,idd):
    obj=Department.objects.get(dept_id=idd)
    obj.status="Rejected"
    obj.save()
    return vmgdept(request)