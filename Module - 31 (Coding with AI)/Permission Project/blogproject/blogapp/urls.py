from django.urls import path
from . import views

urlpatterns = [
    path('category-entry', views.home, name='home'),
]