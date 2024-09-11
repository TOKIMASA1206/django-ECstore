from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from base.models import Profile
from base.forms import UserCreationForm
from django.contrib import messages
 
 
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
