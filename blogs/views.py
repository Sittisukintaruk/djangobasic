from django.shortcuts import render,redirect
from .models import POST
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def hello(request):
    #Qurey Data from Model
   
    data =  POST.objects.all()
    return render(request,'index.html',{'posts': data})

def page1(request):
  

    rating = 4
    return render(request,'page1.html',
    {'name':'บทความท่องเที่ยวภาคกลาง'})

def createForm(request):
    return render(request,'form.html' )

def addUser(request):
    Username = request.POST['username']
    FirstName = request.POST['firstName']
    LastName = request.POST['lastName']
    Email = request.POST['email']
    Password = request.POST['password']
    Repassword = request.POST['repassword']
    
   
    if Password == Repassword :
        if User.objects.filter(username = Username).exists():
            messages.info(request,'Username นี้มีคนใช้แล้ว')
            return redirect('/createForm') 
        elif User.objects.filter(email = Email).exists():
            messages.info(request,'Email ของคุณนั้นซ้ำกับผู้อื่น')
            return redirect('/createForm') 
        else:
            user =  User.objects.create_user(
                    username=Username,
                    password=Password,
                    email=Email,
                    first_name=FirstName,
                    last_name= LastName
                    )
            user.save()
            return redirect('/') 
    else:
        messages.info(request,'รหัสผ่านไม่ตรงกัน !!')
        return redirect('/createForm') 
   

def loginForm(request):

    return render(request,'login.html') 

def login(request):
    Username = request.POST['username']
    Password = request.POST['password']

    #check username password
    user = auth.authenticate(username = Username , password = Password)
    if user is not None:
        auth.login(request,user)
        return redirect('/')
    else:
        messages.info(request,'Username หรือ รหัสผ่านของคุณไม่ถูกต้อง !!')
        return redirect('/loginForm')    

def logout(request):
    auth.logout(request)
    return redirect('/')
     
