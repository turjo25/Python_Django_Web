from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import TaskForm
from .forms import UserRegForm,UserUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
#Task list
@login_required
def task_list(request):
    #status filter
    status_filter = request.GET.get('status','all')
    #category filter
    category_filter = request.GET.get('category','all')
    tasks = Task.objects.filter(user=request.user)
    
    if status_filter != 'all':
        tasks = tasks.filter(is_completed = (status_filter=='completed'))
    
    if category_filter != 'all':
        tasks = tasks.filter(category = category_filter)#check korbe extra kono category ashbe ki na + existing category filter korbe
    
    completed_tasks = tasks.filter(is_completed = True)
    pending_tasks = tasks.filter(is_completed = False)
    
    return render(request,'task_list.html',{
        'completed_tasks' : completed_tasks,
        'pending_tasks' : pending_tasks,
        'status_filter' : status_filter,
        'category_filter' : category_filter,
    })#je kaj gulo krce shb return korce

#task create
@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)#form database e save hobe na bt model form ta ready database e save howar jonne
            task.user = request.user#je user req kortese
            task.save()# then ekhane eshe save hobe
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request,'task_form.html',{'form':form})
    
#task detail page
#selected task er detail dekhar jonne
@login_required
def task_detail(request, task_id):#edit and delete korar jonne
    task = get_object_or_404(Task,id = task_id,user = request.user )
    return render(request,'task_detail.html',{'task':task})

#task delete
@login_required
def task_delete(request,task_id):
    task = get_object_or_404(Task,id = task_id,user = request.user )
    task.delete()
    return redirect('task_list')

#mark task as completed
@login_required
def task_mark_completed(request, task_id):
    task = get_object_or_404(Task,id = task_id,user = request.user )
    task.is_completed = True
    task.save()
    return redirect('task_list')

#user register
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username,password=password)
#             login(user)
#             return redirect('task_list')
#     else:
#         form = UserCreationForm()
#     return render(request,'register.html',{'form':form})
def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserRegForm(request.POST)
        if form.is_valid():
            # Save user to the database
            user = form.save()
            
            # Log the user in immediately
            login(request, user)
            
            return redirect('task_list')
    else:
        # form = UserCreationForm()
        form = UserRegForm()
    return render(request, 'register.html', {'form': form})

#user profile
@login_required
def profile(request):
    return render(request, "profile.html", {"user": request.user})

# update user 
@login_required
def update_profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("task_list")  # go back to task list after update
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, "update_profile.html", {"form": form})

#pass change
@login_required
def pass_change(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user,data = request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'Password Changed!')
            return redirect('task_list')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request,'pass_change.html',{'form':form})