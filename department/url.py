from django.conf.urls import url
from department import views

urlpatterns = [
    url('depart/',views.department),
    url('viewdept/',views.vdept),
    url('viewmgdept/',views.vmgdept),
    url('remove/(?P<idd>\w+)',views.remove),
     url('reject/(?P<idd>\w+)',views.reject),
    ]

