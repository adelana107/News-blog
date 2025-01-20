from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model



# Create your models here.
class User(AbstractUser):
    username= models.CharField(max_length=200, null=True, unique=True)
    email = models.EmailField(unique=True  ,null=True)
    bio = models.TextField(null=True)
    hobbies = models.CharField(max_length=255, blank=True, null=True)
    experience = models.TextField(null=True)
    phone = models.CharField(null=True, max_length=11)
    social = models.TextField(null=True)
    


    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
 
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


    
    
 



class Post(models.Model):
    profile = models.ForeignKey('Profile', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ManyToManyField('Category')
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    date_posted = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f"{self.title} - profile: {self.profile.name}"  # Adjusted to reflect single editor


    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name    
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    email = models.EmailField()
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='editor_profile', null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='images/', default='images/default.jpg')
    date_posted = models.DateTimeField(auto_now_add=True)
    social_link = models.URLField()
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    hobbies = models.CharField(max_length=100)
    bio = models.TextField()
    experience = models.TextField()
    total_views = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    
    def get_full_name(self):
        return self.user.username
    

