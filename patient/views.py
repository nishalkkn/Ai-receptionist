from django.http import HttpResponseRedirect
from django.shortcuts import render
from patient.models import Patient

# Create your views here.
def patient(request):
    ss = request.session["uid"]
    if request.method=='POST':
        obj=Patient()
        obj.name=request.POST.get('an')
        obj.age=request.POST.get('en')
        obj.gender=request.POST.get('gender')
        obj.address=request.POST.get('ao')
        obj.phone_no=request.POST.get('pn')
        obj.user_id = ss
        obj.save()
        return HttpResponseRedirect('/temp/user/')
    return render(request,'patient/patient.html')


def vpnt(request):
    obj = Patient.objects.all()
    context = {
        'x': obj
    }
    return render(request,'patient/view_patient.html',context)


def view_patient_admin(request):
    obj = Patient.objects.all()
    context = {
        'x': obj
    }
    return render(request,'patient/view_patient_admin.html',context)