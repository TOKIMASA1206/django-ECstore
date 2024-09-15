from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from base.models import Profile
from base.forms import UserCreationForm, ContactForm
from django.contrib import messages
from django.urls.base import reverse_lazy
from django.shortcuts import redirect
from django.core.mail import BadHeaderError
from django.views.generic.edit import FormView
 
 
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = '/login/'
    template_name = 'pages/signup.html'
 
    def form_valid(self, form):
        messages.success(self.request, 'Registration complete!  Please log in.')
        return super().form_valid(form)
 
 
class Login(LoginView):
    template_name = 'pages/login.html'
 
    def form_valid(self, form):
        messages.success(self.request, 'Successfully logged in.')
        return super().form_valid(form)
 
    def form_invalid(self, form):
        messages.error(self.request, 'Failed to log in due to an error.')
        return super().form_invalid(form)
 
 
class AccountUpdateView(LoginRequiredMixin,UpdateView):
    model = get_user_model()
    template_name = 'pages/account.html'
    fields = ('username', 'email',)
    success_url = '/account/'
 
    def get_object(self):
        # URL変数ではなく、現在のユーザーから直接pkを取得
        self.kwargs['pk'] = self.request.user.pk
        return super().get_object()
 
 
class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    model = Profile
    template_name = 'pages/profile.html'
    fields = ('name', 'zipcode', 'prefecture',
              'city', 'address1', 'address2', 'tel')
    success_url = '/profile/'
 
    def get_object(self):
        # URL変数ではなく、現在のユーザーから直接pkを取得
        self.kwargs['pk'] = self.request.user.pk
        return super().get_object()
    
    
    
    


class ContactFormView(LoginRequiredMixin, FormView):
    template_name = "pages/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact_result")

    def form_valid(self, form):
        try:
            form.send_email()
            messages.success(self.request, 'Your message has been sent successfully!')
            self.request.session['contact_status'] = 'success'  
            return super().form_valid(form)
        except BadHeaderError:
            messages.error(self.request, 'Invalid header found.')
            self.request.session['contact_status'] = 'failure'  
            return redirect('contact_failure')
        except Exception as e:
            messages.error(self.request, 'An error occurred: {}'.format(e))
            self.request.session['contact_status'] = 'failure' 
            return redirect('contact_failure')

class ContactResultView(LoginRequiredMixin, TemplateView):
    template_name = "pages/contact_result.html"
    
    def dispatch(self, request, *args, **kwargs):
        
        if request.session.get('contact_status') != 'success':
            return redirect('contact')
        del request.session['contact_status']
        return super().dispatch(request, *args, **kwargs)
    

class ContactFailureView(LoginRequiredMixin, TemplateView):
    template_name = "pages/contact_failure.html" 
    
    def dispatch(self, request, *args, **kwargs):

        if request.session.get('contact_status') != 'failure':
            return redirect('contact')
        del request.session['contact_status']
        return super().dispatch(request, *args, **kwargs)