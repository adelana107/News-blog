from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from django.contrib.auth.signals import user_logged_in
import logging
from django.contrib.sessions.models import Session
from datetime import timedelta




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
        return f"{self.title} - profile: {self.profile.user.username}"  # Adjusted to reflect single editor


    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User is required
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')  # Link to the post
    body = models.TextField(max_length=1000)  # Main content of the comment (with length limit)
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE
    )  # For nested replies
    date_posted = models.DateTimeField(default=now)  # When the comment was posted

    class Meta:
        ordering = ['-date_posted']  # Show latest comments first

    def __str__(self):
        return f"{self.user.username} - {self.body[:30]}"  # Commenter's username and snippet
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='editor_profile', null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='images/', default='images/default.jpg')
    date_posted = models.DateTimeField(auto_now_add=True)
    social = models.URLField()
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    hobbies = models.CharField(max_length=100)
    bio = models.TextField()
    experience = models.TextField()
    total_views = models.IntegerField(default=0)
    total_views = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    
    def get_full_name(self):
        return self.user.username
    
class UserLoginSession(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="login_sessions")
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    login_date = models.DateTimeField(default=now)

# Signal to capture login events
def capture_login(sender, request, user, **kwargs):
    # Get the user's IP address
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')

    # Check for an existing session with the same IP and within 1 hour
    one_hour_ago = now() - timedelta(hours=1)
    existing_session = UserLoginSession.objects.filter(
        user=user, 
        ip_address=ip, 
        login_date__gte=one_hour_ago
    ).exists()

    if not existing_session:
        # Create a login session if no duplicate exists in the past hour
        UserLoginSession.objects.create(user=user, ip_address=ip, login_date=now())

# Connect the signal
user_logged_in.connect(capture_login)