from django.conf.urls import url
from temp import views
urlpatterns = [
    url('admin/',views.admin),
    url('user/', views.user),
    url('doctor/', views.doctor),
    url('home/', views.home),
    url('user_he/', views.user_home),
    url('dr_hme/', views.dr_hme),
    url('admn_hm/', views.admn_hm),

]