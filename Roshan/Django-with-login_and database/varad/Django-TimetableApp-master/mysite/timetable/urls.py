from django.conf.urls import url
from . import views

app_name = 'timetable'

urlpatterns = [
    url(r'^(?P<day>[a-zA-Z]+)/$', views.index, name='index'),
    url(r'^create_task/$', views.create_task, name='create_task'),
]
