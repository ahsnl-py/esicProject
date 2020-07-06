from django.forms import ClearableFileInput
from django.contrib.auth.models import User
from django import forms

from .models import Post, PostFile, PostImage

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subject_name', 'body', 'status']


class FileModelForm(forms.ModelForm):
    class Meta:
        model = PostFile 
        fields = ['file']
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True}),
        }

