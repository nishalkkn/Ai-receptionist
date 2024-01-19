from django.conf.urls import url
from patient import views

urlpatterns = [
    url('patient/',views.patient),
    url('viewp/',views.vpnt),
    url('view_patient_admin/',views.view_patient_admin),

]