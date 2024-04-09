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

def loginview(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            print(user)
            if user is not None and user.is_admin:
                print("111111")
                login(request, user)
                print("2222222")
                return redirect('adminpage')
            elif user is not None and user.is_employe:
                login(request, user)
                return redirect('employepage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customerpage')
            else:
                msg = 'Invalid Credentials'
        else:
            msg = "Error Validations Form"
    return render(request, 'login.html', {'form':form, 'msg':msg})

def admin(request):
    return render(request, 'admin.html')

def customer(request):
    return render(request, 'customer.html')

def employee(request):
    return render(request, 'employee.html')