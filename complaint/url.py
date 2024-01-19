from django.conf.urls import url
from complaint import views

urlpatterns =[
    url('complaint/',views.complaint),
    # url('reply/',views.reply),
    url('viewcompt/',views.vcom),
    url('viewreply/',views.vre),
    url('reply/(?P<idd>\w+)',views.reply),

    ]