from django import forms
from .models import ChatForum 

MAX_FORUM_LENGTH = 240


class ForumForm(forms.ModelForm):
    class Meta:
        model = ChatForum 
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_FORUM_LENGTH:
            raise forms.ValidationError("This post is too long")
        return content