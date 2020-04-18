from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):
    # comment_text = forms.CharField(widget = forms.Textarea(attrs={'rows':'3'}))
    class Meta:
        model = Comment
        fields = ['author_comment', 'comment_text']
