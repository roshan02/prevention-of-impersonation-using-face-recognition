from django.shortcuts import render
from django import forms
import MySQLdb
from django.contrib.auth import login, authenticate
from personal.forms import LoginForm


def index(request):
	class NameForm(forms.Form):
		your_name = forms.ImageField(label='snapshot', max_length=100)
		print(your_name)
	return render(request, "personal/home.html")

def contact(request):
	return render(request, "personal/basic.html", {'content': ['If you would like to contact me just email me', 'dn.roshan2@gmail.com']})

def success(request):
	return render(request, "personal/login_success.html")
def center_list(request):
    db = MySQLdb.connect(user='root', db='django',  passwd='roshan', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT password FROM admin_table where adminId = 1')
    centerId = [row[0] for row in cursor.fetchall()]
    db.close()    
    return render(request, 'personal/show.html',  {'centerId': centerId})

"""def login(request):
   username = "not logged in"
   if request.method == "POST":
     MyLoginForm = LoginForm(request.POST)
     if MyLoginForm.is_valid():
       username = MyLoginForm.cleaned_data.get('username')
       raw_password = MyLoginForm.cleaned_data.get('password')
       user = authenticate(username=username, password=raw_password)
       db = MySQLdb.connect(user='root', db='django',  passwd='rutuja8079', host='localhost')
       cursor = db.cursor()
       cursor.execute('SELECT password FROM admin_table where adminId = %s', [username])
       password = [row[0] for row in cursor.fetchall()]
       args = {'password1' : password, 'password2' : raw_password, 'username' : username}
       db.close()     
   else:
      MyLoginForm = Loginform()
   return render(request, 'personal/show.html',  args)"""
#def showtable(request):
def showtable(request):
    conn = MySQLdb.connect(user="root", passwd="rutuja8079", db="django",  host='localhost')
    cur = conn.cursor()

    cur.execute("SELECT * FROM student")
    #row = cur.fetchone()
    rows = cur.fetchall()
    print(rows)
   # args = []
    rollno = []
    name= []
    status = []
    remark = []
    for col in rows:
      rollno.append(col[0])
      name.append(col[1])
      status.append(col[2])
      remark.append(col[3])
    #for(i in range())
      #print(username[])
    l = len(rollno)
    print(l)
   # print(username)
    args = {'rollno' : rollno, 'name' : name, 'status' : status, 'remark' : remark, 'len': range(l) }
    #  args.append(arg)
    cur.close()
    conn.close()
    return render(request, 'personal/report.html',  args)

