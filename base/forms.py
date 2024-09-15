from django import forms
from django.contrib.auth import get_user_model
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse
 
 
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
