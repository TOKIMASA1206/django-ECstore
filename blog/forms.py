from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'published', 'featured_image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter article title',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter article content',
            }),
            'featured_image': forms.FileInput(attrs={
                'class': 'form-control',
            }),
        }