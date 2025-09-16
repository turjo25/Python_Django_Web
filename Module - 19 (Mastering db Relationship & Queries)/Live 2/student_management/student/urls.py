from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('view/', views.list_students,name='list_students'),
    path('create/', views.students_create,name='create_students'),
    path('update/<int:id>', views.update_student,name='update_student'),
    path('delete/<int:id>', views.delete_student,name='delete_student'),
]