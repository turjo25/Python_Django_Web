from django import forms
from .models import Book,Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BookCreationForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','description','authors','category','cover_image','tag']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

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