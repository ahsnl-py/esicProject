from django import forms

from .models import Forum 

MAX_POST_LENGTH = 240


class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum 
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_POST_LENGTH:
            raise forms.ValidationError("This post is too long")
        return content