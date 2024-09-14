# views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import RedirectView
from django.shortcuts import render

class AboutIndexView(LoginRequiredMixin, RedirectView):
    # リダイレクト先のURL
    url = '/about-page/'

    def get_redirect_url(self, *args, **kwargs):
        # ログインしていない場合のリダイレクト先
        if not self.request.user.is_authenticated:
            return '/login/'
        return super().get_redirect_url(*args, **kwargs)



def AboutPageView(request):
    return render(request, 'pages/about.html')

