from django.shortcuts import render
from django import forms
from django.http import HttpResponse
import time
from PIL import Image

def index(request):
	questions = None
	if request.GET.get('search'):
		search = request.GET.get('search')
		abc = request.GET.get('image')
		print(search)
		print(abc)
	if request.GET.get('imgBase64'):
		a = request.GET.get('imgBase64', None)
		print(a)
	#images = Image.objects.all()
	#print(images)
	#time.sleep(10)
	#image_data = open("/home/roshan/python/roshan.jpg", "rb").read()
	#return HttpResponse(image_data, content_type="image/png")
	return render(request, "personal/home.html")

def contact(request):
	return render(request, "personal/basic.html", {'content': ['If you would like to contact me just email me', 'dn.roshan2@gmail.com']})

# Create your views here.
