from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import Blogpost, User
from .forms import PostForm, SignForm, LoginForm
from django.utils import timezone
from passlib.hash import pbkdf2_sha256
from django.contrib.auth import logout as auth_logout, login as auth_login,authenticate
# Create your views here.
from django.conf import settings
from django.utils.timezone import now
from django.contrib import messages
from django import forms

def index(request):
    posts = Blogpost.objects.all().order_by('date_posted').reverse()

    print("request.user="+request.session.get('logged'))
    return render(request,'index.html',{'posts': posts,'username': request.session.get('logged')})

def about(request):
    return render(request,'about.html')

@login_required(login_url='/login')
def add(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post= form.save(commit=False)
            title=form.cleaned_data['title']
            subtitle=form.cleaned_data['subtitle']
            content=form.cleaned_data['content']
            author=form.cleaned_data['author']

            post.date_posted  = now()

            post.save()
            form=PostForm()
            return redirect('/index')
    else:
        form=PostForm()
    return render(request, 'add.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            username  = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password_hash']
            pwd = User.encrypt_password(password)
            if User.objects.filter(username=username):
                messages.error(request,'This username already exists')
                return redirect('signup')
            if len(password) <6:
                messages.error(request,'Password too much short')
                return redirect('signup')
            user_obj = User(username=username,email=email, password_hash=pwd)
            user_obj.save()

            return redirect('/index')
        else:
            messages.error(request,'email incorrect')
            return redirect('signup')
    else:
            form=SignForm()
    return render(request,'signup.html', {'form':form})


def login(request):
        user1 = None
        username = 'not logged in'
        form= LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password_hash']
            #user=User.objects.filter(username=username)
            try:
              user1= User.objects.get(username=username)
            except User.DoesNotExist:
                pass
            if user1 is None or not user1.check_password(password):

               messages.error(request, "Your credentials are invalid! Retry please..")
               print("sbagliate")
            else:
              user = form.get_user()
              auth_login(request, user)
              request.session['logged'] = user1.username
              print ("session: "+request.session['logged'])
              print("corrette")

              return redirect('/index', )

        return render(request, 'login.html')

def logout(request):
    user = request.user

    auth_logout(request,user)
    try:
      del request.session['logged']
    except:
      pass

    return redirect('/index')
