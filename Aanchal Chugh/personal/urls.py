from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [

    url(r'^$', views.index, name = 'index'),
    url(r'^contact/', views.contact, name= 'contact'),	
	url(r'^success/', views.success, name= 'success'),

]
