from django.shortcuts import render,redirect,get_object_or_404
from . import models
from . import forms
from django.contrib import messages
from django.db import connection
from django.db.models import Count,Avg,Max,Min,Sum

#for class based view
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

# name,email,age,photo --> model design

# viwes will handle them:
# showlist,add,update,delete

#template with minimal design

# showlist
def list_students(request):
    students = models.Student.objects.all();
#optimization
    # one_to_many_opt = models.Student.objects.select_related('department').all()
    # many_to_many_opt = models.Student.objects.prefetch_related('course').all()
#order by
    # course = models.Course.objects.order_by('id').all()
    # for i in course:
    #     print(i.id,i.title)
# raw sql
    # studentss = models.Student.objects.raw("""SELECT * FROM student_student""")
    # this is so complex and we normally don't use it
    
# connection related sql
    # cursor = connection.cursor()
    # cursor.execute("""SELECT * FROM student_student""")
    # rows = cursor.fetchall()
    # print(rows)
# annotation and aggregation
    ag_st = models.Student.objects.aggregate(total=Min('id'))
    print(ag_st)
    st_an = models.Student.objects.annotate(st_cnt = Max('id'))
    for i in st_an:
        print(i.name,i.department,i.st_cnt)
    print(st_an)
    
    return render(request,'student_list.html',{'students':students})




#class based showlist
# class StudentListView(ListView):
#     template_name = 'student_list.html'
#     model = models.Student
#     context_object_name = 'students'
    

# def students_create(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         age = request.POST.get('age')
#         email = request.POST.get('email')

#         models.Student.objects.create(
#             name = name,
#             age = age,
#             email = email
#         )
#         return redirect('list_students')
#     return render(request,'student_create.html')

#creating model form
# def students_create(request):
#     if request.method == 'POST':
#         form = forms.StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
            
#             # message framework:
#             messages.success(request,'Student added successfully!')
            
#             return redirect('list_students')
#     form = forms.StudentForm()
#     return render(request,'student_create.html',{'form':form})
#class based create student
class StudentCreateView(CreateView):
    model = models.Student
    form_class = forms.StudentForm
    template_name = 'student_create.html'
    success_url = reverse_lazy('list_students')
    
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        messages.success(self.request,'Student added successfully!')
        return super().form_valid(form)
    

#updating student
# def update_student(request,id):
#     student = get_object_or_404(models.Student,id = id)
#     if request.method == 'POST':
#         form = forms.StudentForm(request.POST,instance=student)
#         if form.is_valid():
#             form.save()
            
#             # message framework:
#             messages.success(request,'Student updated successfully!')
            
#             return redirect('list_students')
#     form = forms.StudentForm(request.POST or None,instance=student)
#     return render(request,'student_create.html',{'form':form, 'isUpdated':True})
#class base update
class StudentUpdateView(UpdateView):
    model = models.Student
    form_class = forms.StudentForm
    template_name = 'student_create.html'
    success_url = reverse_lazy('list_students')
    
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        messages.success(self.request,'Student updated successfully!')
        return super().form_valid(form)

#deleting student
# def delete_student(request,id):
#     student = get_object_or_404(models.Student,id = id)
#     student.delete()
    
#     # message framework:
#     messages.success(request,'Student deleted successfully!')
    
#     return redirect('list_students')
#class based delete(kaj kore na)
class StudentDeleteView(DeleteView):
    model = models. Student
    template_name ='student_delete.html'
    success_url = reverse_lazy('list_students')
    pk_url_kwarg = 'id'

    def delete(self, request, *args, ** kwargs):
        messages.success(self.request, 'Student deleted Successfully')
        return super().delete(request, *args, ** kwargs)
