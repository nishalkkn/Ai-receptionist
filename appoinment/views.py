from django.http import HttpResponseRedirect
from django.shortcuts import render
from appoinment.models import Appointment
from doctor.models import Doctor
from patient.models import Patient
# Create your views here.

def appoinment(request):
    ss = request.session["uid"]
    obb=Doctor.objects.all()
    obj=Patient.objects.filter(user_id=ss)
    context={
        'x':obb,
        'y':obj
    }
    if request.method=='POST':
        obj=Appointment()
        obj.doc_id=request.POST.get('dnm')
        obj.patient_id=request.POST.get('pname')
        obj.date=request.POST.get('ps')
        obj.time=request.POST.get('pd')
        obj.status='pending'
        obj.save()
        return HttpResponseRedirect('/temp/user/')
    return render(request,'appoinment/appoiment.html',context)



def vapp(request):
    ss=request.session["uid"]
    obj=Appointment.objects.filter(doc_id=ss)
    context={
        'x':obj
    }
    return render(request,'appoinment/view_appointment.html', context)

def approve(request,idd):
    obj=Appointment.objects.get(appot_id=idd)
    obj.status="Approved"
    obj.save()
    return vapp(request)

def reject(request,idd):
    obj=Appointment.objects.get(appot_id=idd)
    obj.status="Rejected"
    obj.save()
    return vapp(request)


def v_app_appoinment(request):
    ss = request.session["uid"]
    obj=Appointment.objects.filter(patient_id=ss, status= "Approved")
    context={
        'x':obj
    }
    return render(request,'appoinment/viw_apved_appoinment.html', context)

