from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('reg/', views.reg_view,name='registration'),
    path('login/', views.login_view,name='login'),
    path('logout/', views.logout_view,name='logout'),
    path('passChng/', views.pass_change,name='passChng'),
    path('passChng2/', views.pass_change2,name='passChng2'),
]