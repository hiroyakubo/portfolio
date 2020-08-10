from django import forms

from accounts.models import CustomUser
from .models import Tweet, Comment


class UsernameForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            "username",  
        ]

class EmailForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            "email",  
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            "age", 
            "photo",  
        ]

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = [
            "tweet", 
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "comment_item", 
        ]
