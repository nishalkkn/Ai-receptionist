from django.shortcuts import render

# Create your views here.

def admin(request):
    return render(request,'temp/admin.html')

def user(request):
    return render(request,'temp/user.html')

def doctor(request):
    return render(request,'temp/doctor.html')

def home(request):
    return render(request,'temp/home.html')

def user_home(request):
    return render(request,'temp/user_home.html')

def dr_hme(request):
    return render(request,'temp/dr_hme.html')

def admn_hm(request):
    return render(request,'temp/admn_hme.html')