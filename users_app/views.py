from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import CustomRegisterForm

def register(request):
    if request.method == "POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New User Account Created, Login To Get Started!"))
            return redirect('register')
    else:
        register_form = CustomRegisterForm()
    return render(request,"register.html", {'register_form': register_form})

def login_view(request):
     if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('todolist')
        else:
            return render(request, "login.html", {'form': form})
     else:
         form = AuthenticationForm()
         return render(request, "login.html", {'form': form})   
                
def logout_view(request):
    logout(request)
    return render(request, "logout.html", {})    


    


        

