from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# 1. Category 
# 2. Tag
# 3. Author
# 4. Book
# 5. comment

class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    authors = models.ManyToManyField(Author, related_name='books')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True,null=True,default=None)
    tag = models.ManyToManyField(Tag)
    view_content = models.PositiveBigIntegerField(default=0)
    
    def __str__(self):
        return self.title
   
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
