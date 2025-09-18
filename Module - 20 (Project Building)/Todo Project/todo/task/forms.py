from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['user']#user bad e shb
        # field = [] eikhan e shb field dite hbe jegula amader drker
        
        widgets = {
            'due_date': forms.DateInput(attrs={'type':'date'}),
            'due_time': forms.TimeInput(attrs={'type':'time'}),
        }#from end er html e time and date akare field 2 ta show koranor jonne

class UserRegForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]