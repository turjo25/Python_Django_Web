from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        # exclude = [] eita diye form e kon kon field amar lagbe na ta define kora  jabe