from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    
    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author,related_name='books',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    published_date = models.DateField()
    
    def __str__(self):
        return self.title

