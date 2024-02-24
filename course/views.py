from django.shortcuts import render,redirect
from .models import course
from .models import student_details
from django.contrib.auth.models import auth,User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'index.html')
def function(request):
    data=course.objects.all()
    cou={
        'data':data
    }
    return render(request,'available.html',context=cou)
def student(request):
    data= student_details.objects.all()
    cou={
        'data':data
    }
    return render(request,'student.html',context=cou)

def register(request):
    if request.method=="POST":
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        username=request.POST["username"] 
        email=request.POST["email"]
        password=request.POST["password"]
        user=auth.authenticate(firstname=firstname,lastname=lastname,username=username,email=email,password=password)
        user=User.objects.create_user(
            first_name=firstname,
            last_name=lastname,
            username=username,
            email=email,
            password=password,

        )
        user.save()
        return redirect('/templates/new.html')

    return render(request,'register.html')

def register1(request):
    if request.method=="POST":
        fullname=request.POST["fullname"]
        email=request.POST["email"]
        duration=request.POST["duration"] 
        mobile_no=request.POST["mobile_no"]
        course=request.POST["course"]
        slot=request.POST["slot"]
        seats=request.POST["seats"]
        use=student_details(fullname=fullname,email=email,duration=duration,mobile_no=mobile_no,course=course,slot=slot,seats=seats)
        use.save()
    return render(request,'register1.html')

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/templates/new.html')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("login")
    else:

        return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def new(request):
    return render(request,'new.html')

def contact(request):
    return render(request,'contact.html')















