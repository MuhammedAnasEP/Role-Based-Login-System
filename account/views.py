from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')

        else:
            msg = 'Form is not valid'
    
    else:
        form = SignupForm()
    return render(request, 'register.html', {'form':form, 'msg':msg})

def login(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                msg = 'Invalid Credentials'
        else:
            msg = "Error Validations Form"
    return render(request, 'login.html', {'form':form, 'msg':msg})

def home(request):
    return render(request, 'homepage.html')