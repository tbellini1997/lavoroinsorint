from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm,LoginForm, BookForm
from .models import User, Car, CarBook
from django.contrib import messages
from passlib.hash import pbkdf2_sha256
from django.contrib.auth import authenticate, login as logg, logout as loggout

# Create your views here.
def details(request,id):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:

        form = BookForm(request.POST)
        # check whether it's valid:

        if form.is_valid():
            cars=Car.objects.filter(id=id)
            print(cars)
            frombooked=form.cleaned_data['frombooked']
            tobooked=form.cleaned_data['tobooked']
            note=form.cleaned_data['note']

            u=request.session["current"]
            u2=User.objects.filter(username=u)
            print(u2)
            newbook=CarBooked(frombooked=frombooked, tobooked=tobooked,note=note,username=self,model=cars.model)
            newbook.save()


    else:
        form = BookForm()
    cars=Car.objects.filter(id=id)
    print(id)

    return render(request,'detailscar.html',{'cars':cars,'form':form})

def index(request):
    cars=Car.objects.all()
    u=request.session["current"]

    return render(request,'index.html',{'cars':cars,'utente':u})



def authss(username=None, password=None):
    try:
        user = User.objects.get(username=username)
        if user.check_password(password):
            return user
    except User.DoesNotExist:
        return None

def login(request):


    if request.method == 'POST':
        # create a form instance and populate it with data from the request:

        form = LoginForm(request.POST)
        # check whether it's valid:

        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user=authss(username=username,password=password)
            print(user)
            if user is not None:
              if not request.user.is_authenticated:
                print("login?")
                request.session["current"] = user.username
                print(user.username)
                u=user.username
                return redirect('index')
            else:
                messages.error(request,'Credentials invalid')
                return redirect('login')
    else:
        form = LoginForm()

    return render(request,'login.html',{'form':form})

def logout(request):
    try:
        del request.session['current']
        print("sloggato")

    except KeyError:
        pass
    return redirect('login')

def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            pwd = User.encrypt_password(password)
            searchuser= User.objects.filter(username=username)
            if searchuser:
                messages.error(request,'This username already exists')
                return redirect('register')
            else:
                newuser=User(first_name=first_name, last_name=last_name,username=username,email=email,password=pwd)
                newuser.save()

                return redirect('/login')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request,'register.html', {'form':form})
