from django.shortcuts import render
from django.http import HttpResponse
from . models import Blog

# Create your views here.
# def home(request):
#     return HttpResponse("<h1>Home page</h1>")

# def home(request):
#         return render(request,"index.html")

def home(request):
        a = 12
        b = {'name':'turjo','age':25}
        return render(request,"index.html",context={'a':a,'b':b})


# def home(request):
#         return render(request,'index.html')

def about(request):
    blogs = Blog.objects.all() #blog model er shb object niye ashte bola hocce 
    return render(request,"about.html",context={'blogs':blogs})
