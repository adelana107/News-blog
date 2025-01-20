# forms.py
from django import forms
from .models import Comment, User, Post, Profile
from django.contrib.auth.forms import UserCreationForm





class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].widget = forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'})


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Search')



class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'avatar', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'bio', 'phone', 'avatar', 'hobbies', 'experience', 'social_link']  # Include fields you want to update


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'image']  # Add 'category' and 'editor' fields

    # You can customize widgets if needed (e.g., adding a file input for image)
    image = forms.ImageField(required=False)