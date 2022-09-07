import email
from turtle import title
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=17)
    subject=models.CharField(max_length=100)
    details=models.TextField()
    
    def __str__(self):
        return self.name
class BlogPost(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="blog_post")
    title=models.CharField(max_length=100)
    details= models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
