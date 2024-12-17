from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = [
            "post",
            "date",
        ]
        labels = {
            "username": "Enter Your Name",
            "user_email": "Enter Your Email Address",
            "text": "Add a Comment...",
        }
