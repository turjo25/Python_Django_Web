from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blogapp.common_func import CheckUserPermission
# Create your views here.



@login_required
def home(request):
    if CheckUserPermission(request, "can_view", "/category-entry"):
        return render(request, 'blog/403.html')

    return render(request,'category/insert.html')