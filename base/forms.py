from django import forms
from django.contrib.auth import get_user_model
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import Item, Image, Category, Tag
 
 
class UserCreationForm(forms.ModelForm):
    password = forms.CharField()
 
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', )
 
    def clean_password(self):
        password = self.cleaned_data.get("password")
        return password
 
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user 




class ContactForm(forms.Form):
    name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "name",
        }),
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': "e-mail",
        }),
    )
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': "Message",
        }),
    )

    def send_email(self):
        subject = "Message"
        message = self.cleaned_data['message']
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        from_email = '{name} <{email}>'.format(name=name, email=email)
        recipient_list = [settings.EMAIL_HOST_USER]
        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")
        
        

# 店舗側 商品追加用

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']  # 'slug' は自動生成されるため除外
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category name',
            }),
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']  # 'slug' は自動生成されるため除外
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter tag name',
            }),
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'stock', 'description', 'is_published', 'category', 'tags']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product name',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price',
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter stock quantity',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product description',
                'rows': 3,
            }),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'tags': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input',
            }),
        }

# Image用のフォームセット


class ImageForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Image
        fields = ['image']

ImageFormSet = inlineformset_factory(
    Item,
    Image,
    form=ImageForm,
    fields=['image'],
    extra=3,
    can_delete=True,
    widgets={
        'id': forms.HiddenInput(),
        'item': forms.HiddenInput(),
        'image': forms.ClearableFileInput(attrs={
            'class': 'form-control-file',
        }),
    },
)
