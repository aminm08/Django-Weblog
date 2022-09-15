from django import forms

from .models import BlogPost, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'short_description', 'text', 'status']
        widgets = {
            'short_description': forms.Textarea(attrs={'rows':4,'cols':15}),
            # 'text': forms.Textarea(attrs={'rows': 10, 'cols': 15})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'rating']
