from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from medical_record.models import MedicalRecord
from patient.models import Patient
from doctor.models import Doctor
from appoinment.models import Appointment
from user import views



# Create your views here.
def medical_record(request):
    ss=request.session["uid"]
    obb=Appointment.objects.filter(doc_id=ss)
    context={
        'z':obb
    }

    if request.method=='POST':
        obj=MedicalRecord()
        obj.doct_id=ss
        obj.appo_id=request.POST.get("ap")
        myfile = request.FILES['report']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.med_recd = myfile.name
        obj.save()
        return HttpResponseRedirect('/temp/doctor/')
    return render(request,'medical_record/medicalrecord.html',context)


def vmedre(request):
    ss=request.session["uid"]
    obj = MedicalRecord.objects.filter(doct_id=ss)
    context = {
        'x': obj
    }
    return render(request,'medical_record/view_medicalrecord.html',context)



def update(request,idd):
    obb=MedicalRecord.objects.get(record_id=idd)
    context={
        'x':obb
    }
    if request.method=='POST':
        obj=MedicalRecord.objects.get(record_id=idd)
        myfile = request.FILES['report']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.med_recd = myfile.name
        obj.save()
        return vmedre(request)
    return render(request,'medical_record/update.html',context)


def view_med_report_user(request):
    ss=request.session["uid"]
    obb=MedicalRecord.objects.filter(appo__patient__user_id=ss)
    context = {
        'a':obb
    }
    return render(request,'medical_record/view_med_report_user.html',context)

