from django import forms
from .models import BlogPost
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'published', 'featured_image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': 'Enter article title',
            }),
            'content': CKEditorUploadingWidget(),
            'featured_image': forms.FileInput(attrs={
                'class': 'form-control',
                'required': True,
            }),
        }