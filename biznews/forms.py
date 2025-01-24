# forms.py
from django import forms
from .models import Comment, User, Post, Profile
from django.contrib.auth.forms import UserCreationForm



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']  # Include only the body field for the comment

    def clean_body(self):
        body = self.cleaned_data.get('body')
        if len(body) > 1000:
            raise forms.ValidationError("Comment cannot exceed 1000 characters.")
        return body


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']  # Only the body field is necessary for a reply

    def clean_body(self):
        body = self.cleaned_data.get('body')
        if len(body) > 1000:
            raise forms.ValidationError("Reply cannot exceed 1000 characters.")
        return body



class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Search')



class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'avatar', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'first_name', 'last_name', 'email', 'bio', 'phone', 'avatar', 'hobbies', 'experience', 'social']  # Include fields you want to update


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'image']  # Add 'category' and 'editor' fields

    # You can customize widgets if needed (e.g., adding a file input for image)
    image = forms.ImageField(required=False)


