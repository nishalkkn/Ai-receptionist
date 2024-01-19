from django.conf.urls import url
from doctor import views

urlpatterns = [
    url('doct/',views.doctor),
    url('view/',views.vdoct),
    url('view_dr_user', views.v_doct_user),

]