from django.shortcuts import render
from django import forms
from django.http import HttpResponse
import MySQLdb
from django.contrib.auth import login, authenticate
from personal.forms import LoginForm


import base64
import cv2
import re
import face_recognition
import pyttsx3
engine = pyttsx3.init()

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True


def recognize(img, mis):
	#fp = open("names.txt", "r+")
	#name = fp.readline()
	load_face_encodings = []
	names = []
	mis = mis + ".jpg"
	"""while(name):
		name = name.strip()
		names.append(name)
		load = face_recognition.load_image_file(name)
		load_face_encodings.append(face_recognition.face_encodings(load)[0])
		name = fp.readline()"""
	names.append(mis)
	load = face_recognition.load_image_file(mis)
	load_face_encodings.append(face_recognition.face_encodings(load)[0])


	# Initialize some variables
	face_locations = []
	face_encodings = []
	face_names = []
	process_this_frame = True

	
	# Grab a single frame of video
	frame = img

	# Resize frame of video to 1/4 size for faster face recognition processing
	small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

	# Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
	rgb_small_frame = small_frame[:, :, ::-1]

	# Only process every other frame of video to save time
	if process_this_frame:
		# Find all the faces and face encodings in the current frame of video
		face_locations = face_recognition.face_locations(rgb_small_frame)
		face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

		face_names = []
		for face_encoding in face_encodings:
			# See if the face is a match for the known face(s)
			n = 0

			matches = face_recognition.compare_faces(load_face_encodings, face_encoding)
			name = "Unknown"

			if True in matches:
				first_match_index = matches.index(True)
				name = names[first_match_index]
				name = name[0:len(name) -4]
				#engine.say("Hello " + name+ "Verification completed")
				engine.say("Hi " + name)
				print("Match Found")
				engine.runAndWait() 
				return True
			face_names.append(name)



def index(request):
	print("Hello")
	questions = None
	mis="111507047"
	if request.POST.get('mis',''):
		mis = request.POST.get('mis')
		print(mis)
	if request.POST.get('image', ''):
		data = request.POST.get('image')
		dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
	#image_data = self.cleaned_data['image_data']
		image_data=data
		image_data = dataUrlPattern.match(image_data).group(2)
		image_data = image_data.encode()
		image_data = base64.b64decode(image_data)
 
		with open('screenshot.jpg', 'wb') as f:
			f.write(image_data)
		img = cv2.imread('screenshot.jpg')
		if(recognize(img, mis)):
			return render(request, "personal/home.html", "Match Successful")
		else:
			return render(request, "personal/home.html", "Match Not Found")


"""def InputView(request):
	if request.POST:
		form = InputForm(request.POST)
		if form.is_valid():
			form.save()

		return HttpResponseRedirect('account/input')
	else:
		form = InputForm()
		args = {'form' : form}
		return render(request,'/accounts/input.html', args)
"""

def contact(request):
	return render(request, "personal/basic.html", {'content': ['If you would like to contact me just email me', 'dn.roshan2@gmail.com']})

def main(request):
	class NameForm(forms.Form):
		your_name = forms.ImageField(label='snapshot', max_length=100)
		print(your_name)
	return render(request, "personal/main.html")
def success(request):
	return render(request, "personal/login_success.html")
def center_list(request):
    db = MySQLdb.connect(user='root', db='admin',  passwd='aanchal@175', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT password FROM admin_table where adminId = 1')
    centerId = [row[0] for row in cursor.fetchall()]
    db.close()    
    return render(request, 'personal/show.html',  {'centerId': centerId})

def login(request):
   print("Hello")
   username = "not logged in"
   if request.method == "POST":
     MyLoginForm = LoginForm(request.POST)
     if MyLoginForm.is_valid():
       username = MyLoginForm.cleaned_data.get('username')
       raw_password = MyLoginForm.cleaned_data.get('password')
       user = authenticate(username=username, password=raw_password)
       db = MySQLdb.connect(user='root', db='admin',  passwd='roshan', host='localhost')
       cursor = db.cursor()
       cursor.execute('SELECT password FROM admin_table where adminId = %s', [username])
       password = [row[0] for row in cursor.fetchall()]
       #password = password[0:len(password)-1]
       pass1 = password[0]
       
       if(pass1 == raw_password):
              db.close()
              return render(request, 'personal/home.html')
       #args = {'password1' : password, 'password2' : raw_password, 'username' : username}
       else:
              return render(request, 'personal/main.html')
   else:
      MyLoginForm = LoginForm()
   return render(request, 'personal/home.html')

# Create your views here.
