from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

USER_ROLES = (
    ('admin','Admin'),
    ('teacher','Teacher'),
    ('student','Student'),
)

class User(AbstractUser): #Abstract base class
    role = models.CharField(max_length=100,choices=USER_ROLES)
    mobile_no = models.CharField(max_length=12)
    #built in user model er shbkicu + ei role and mobile_no
    
    def __str__(self):
        return f"{self.id} {self.username} - {self.role}"