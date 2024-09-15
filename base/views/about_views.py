# views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.shortcuts import render

class AboutIndexView(LoginRequiredMixin, TemplateView):
      template_name = 'pages/about.html'


