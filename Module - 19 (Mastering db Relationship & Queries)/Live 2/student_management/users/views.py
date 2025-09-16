from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
def reg_view(request):
    if request.method == 'POST':
        form = forms.UserRegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,'Account created successfully')
            return redirect('list_students')
    else:
        form = forms.UserRegForm()
    return render(request,'reg.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password = password)
            if user is not None:    
                login(request,user)
                messages.success(request,'Account Login successful')
                return redirect('list_students')
            else:
                messages.error(request,'Invalid Credentials')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    messages.success(request,'Logged out successful')
    return redirect('login')

# method 1: need old password 
@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user,data = request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,form.user)
            return redirect('list_students')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'pass_change.html',{'form':form})

#method 2: no need anything
@login_required
def pass_change2(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user,data = request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'Password Changed!')
            return redirect('list_students')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request,'pass_change.html',{'form':form})