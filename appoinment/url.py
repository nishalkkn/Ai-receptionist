from django.conf.urls import url
from appoinment import views

urlpatterns=[
    url('appoint/',views.appoinment),
    url('viewapp/',views.vapp),
    url('approve/(?P<idd>\w+)',views.approve),
    url('reject/(?P<idd>\w+)',views.reject),
    url('view_app_appoinment/', views.v_app_appoinment),

]