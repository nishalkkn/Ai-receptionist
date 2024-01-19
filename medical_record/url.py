from django.conf.urls import url
from medical_record import views

urlpatterns = [
    url('medrec/',views.medical_record),
    url('viewm/',views.vmedre),
    url('update/(?P<idd>\w+)',views.update),
    url('viw_med_rept_usr/', views.view_med_report_user),

]