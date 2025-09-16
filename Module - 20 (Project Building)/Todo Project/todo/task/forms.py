from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['user']#user bad e shb
        # field = [] eikhan e shb field dite hbe jegula amader drker
        
        widgets = {
            'due_date': forms.DateInput(attrs={'type':'date'}),
            'due_time': forms.TimeInput(attrs={'type':'time'}),
        }#from end er html e time and date akare field 2 ta show koranor jonne