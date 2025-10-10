from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
# 1. Category 
# 2. Tag
# 3. user
# 4. Post
# 5. comment

class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    # comment = models.ForeignKey()
    created_at = models.DateTimeField(auto_now_add=True) #object create korar time ta store hobe automatically
    updated_at = models.DateTimeField(auto_now=True) #object update korar time ta store hobe automatically
    liked_users = models.ManyToManyField(User,related_name='liked_posts')
    view_content = models.PositiveBigIntegerField(default=0)
    
    def __str__(self):
        return self.title
   
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username