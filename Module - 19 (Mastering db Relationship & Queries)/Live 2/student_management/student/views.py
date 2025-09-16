from django.shortcuts import render,redirect,get_object_or_404
from . import models
from . import forms
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.

# showlist
def list_students(request):
    students = models.Student.objects.all()
    return render(request,'student_list.html',{'students':students})

#creating model form
def students_create(request):
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            
            # message framework:
            messages.success(request,'Student added successfully!')
            
            return redirect('list_students')
    form = forms.StudentForm()
    return render(request,'student_create.html',{'form':form})


    

#updating student
def update_student(request,id):
    student = get_object_or_404(models.Student,id = id)
    if request.method == 'POST':
        form = forms.StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            
            # message framework:
            messages.success(request,'Student updated successfully!')
            
            return redirect('list_students')
    form = forms.StudentForm(request.POST or None,instance=student)
    return render(request,'student_create.html',{'form':form, 'isUpdated':True})


#deleting student
def delete_student(request,id):
    student = get_object_or_404(models.Student,id = id)
    student.delete()
    
    # message framework:
    messages.success(request,'Student deleted successfully!')
    
    return redirect('list_students')

