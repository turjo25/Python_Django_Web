from django.contrib import admin
from django.urls import path
from first_app.views import home,about


urlpatterns = [
    path('home/',home),
    path('about/',about), 
]