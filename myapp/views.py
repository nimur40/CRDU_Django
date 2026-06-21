
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



def password_reset_request(request):
    return render(request,"password_reset.html")
def password_reset_confirm(request):
    return render(request,"password_reset_confirm.html")

def password_reset_done(request):
    return render(request,"password_reset_done.html")
def password_reset_complete(request):
    return render(request,"password_reset_complete.html")



def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid username & password")
    return render(request,"login.html")

def user_register(request):
    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password")
        password2 = request.POST.get("confirm_password")

        if password1 != password2:
            messages.error(request, "Password does not match")

        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")

        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")

        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            messages.success(
                request,
                "Account created successfully. You can log in now."
            )
            return redirect("login")

    return render(request, "register.html")
 
@login_required(login_url='/login/')   
def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def home(request):
    return  render(request,"home.html")

@login_required(login_url='/login/')
def expense_create(request):
    return render(request,"expense_form.html")

@login_required(login_url='/login/')
def expense_update(request):
    return render(request,"expense_form.html")

@login_required(login_url='/login/')
def expense_list(request):
    return render(request,"expense_list.html")

@login_required(login_url='/login/')
def expense_delete(request):
    return render(request,"expense_confirm_delete.html")
