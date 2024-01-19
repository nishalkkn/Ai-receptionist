from django.conf.urls import url
from service import views

urlpatterns = [
    url('service/',views.service),
    url('viewser/',views.vser),
    url('remove/(?P<idd>\w+)',views.remove)

]