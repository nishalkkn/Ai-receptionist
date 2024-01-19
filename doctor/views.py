from django.http import HttpResponseRedirect
from django.shortcuts import render
from doctor.models import Doctor
from department.models import Department
from login.models import Login

# Create your views here.
def doctor(request):
    obj=Department.objects.all()
    context={
        'x':obj
    }
    if request.method=='POST':
        obj=Doctor()
        obj.doct_name=request.POST.get('an')
        obj.dept_id=request.POST.get('dpt')
        obj.address=request.POST.get('en')
        obj.phone_no=request.POST.get('pn')
        obj.email=request.POST.get('em')
        obj.experience=request.POST.get('ee')
        obj.qualification=request.POST.get('qn')
        obj.password = request.POST.get('ps')
        obj.save()

        ob=Login()
        ob.user_name=obj.doct_name
        ob.password=obj.password
        ob.type='doctor'
        ob.uid=obj.doct_id
        ob.save()
        return HttpResponseRedirect('/temp/admin/')
    return render(request,'doctor/doctor.html',context)


def vdoct(request):
    obj =Doctor.objects.all()
    context = {
        'x': obj
    }
    return render(request,'doctor/view_doctor.html',context)

def v_doct_user(request):
    obj =Doctor.objects.all()
    context = {
        'x': obj
    }
    return render(request,'doctor/view_dr_user.html',context)