from django.shortcuts import render,redirect
from .forms import * # type: ignore
from django.contrib.auth import logout

# Create your views here.
def index(request):
    msg=""
    if request.method=='POST':

        unm=request.POST['username']
        pas=request.POST['password']

        user=usersignup.objects.filter(username=unm,password=pas) # type: ignore
        if user: #TRUE
            print("Login Successfully!")
            msg="Login Successfully!"

            request.session['user']=unm
            return redirect('home')
        else:
            print("Error!Something went wrong...")
            msg="Error!Something went wrong..."
    return render(request,'index.html',{'msg':msg})

def signup(request):
    if request.method=='POST':
        newuser=signupForm(request.POST) # type: ignore
        if newuser.is_valid():
            newuser.save()
            print("Signup successfully!")
            return redirect('/')
        else:
            print(newuser.errors)
    return render(request,'signup.html')

def home(request):
    user=request.session.get('user')
    return render(request,'home.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')