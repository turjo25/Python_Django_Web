from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('view/', views.list_students,name='list_students'),
    # for class based view
    # path('view/', views.StudentListView.as_view(),name='list_students'),
    
    #path('create/', views.students_create,name='create_students'),
    #for class based
    path('create/', views.StudentCreateView.as_view(),name='create_students'),
    
    # path('update/<int:id>', views.update_student,name='update_student'),
    #for class based update
    path('update/<int:id>', views.StudentUpdateView.as_view(),name='update_student'),
    
    # path('delete/<int:id>', views.delete_student,name='delete_student'),
    #for class based delete
    path('delete/<int:id>', views.StudentDeleteView.as_view(),name='delete_student'),
]