# views.py
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormMixin
from base.models import About, Member
from base.forms import AboutPageForm
from django.contrib import messages

#お客様側の公開ページ
class AboutIndexView(LoginRequiredMixin, TemplateView):
      template_name = 'pages/about.html'
      
      def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 通常は1件だけの想定
        about_item = About.objects.first()
        members = Member.objects.select_related('user').all()
        context['about_item'] = about_item
        context['members'] = members
        return context
    


#店舗オーナーサイドの管理画面
class AboutStoreListView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'store/pages/about/index.html'

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 通常は1件だけの想定
        about_item, created = About.objects.get_or_create(defaults={
        })
        context['about_item'] = about_item
        return context
    
#店舗オーナーサイドのAboutの追加・編集

class AboutStoreUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    template_name = 'store/pages/about/about_form.html'
    form_class = AboutPageForm
    model = About
    success_url = reverse_lazy('store_about')

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        messages.success(self.request, 'Aboutページが更新されました。')
        return super().form_valid(form)
    def form_invalid(self, form):               
        messages.error(self.request, 'Aboutページの更新に失敗しました。')
        return super().form_invalid(form)

  
  
#店舗オーナーサイドのメンバー一覧  
class MemberListView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'store/pages/member/index.html'
    def test_func(self):
        return self.request.user.is_staff
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        members = Member.objects.select_related('user').all()
        context['members'] = members
        return context    
  
#Memberの追加・編集・削除
class MemberCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Member
    fields = ['user', 'profile_image', 'comment', 'position']
    template_name = 'store/pages/member/member_form.html'
    success_url = reverse_lazy('store_members')
    def form_valid(self, form):
        messages.success(self.request, 'メンバーが追加されました。')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, 'メンバーの追加に失敗しました。')
        return super().form_invalid(form)
    

    def test_func(self):
        return self.request.user.is_staff

class MemberUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Member
    fields = ['user', 'profile_image', 'comment', 'position']
    template_name = 'store/pages/member/member_form.html'
    success_url = reverse_lazy('store_members')
    def form_valid(self, form):
        messages.success(self.request, 'メンバーが編集されました。')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, 'メンバーの編集に失敗しました。')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 編集対象のメンバー（インスタンス）をコンテキストに追加
        context['member'] = self.get_object()
        return context      

    def test_func(self):
        return self.request.user.is_staff
  
  
class MemberDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
      model = Member
      template_name = 'store/pages/member/member_confirm_delete.html'
      success_url = reverse_lazy('store_members')
      
      def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          # 編集対象のメンバー（インスタンス）をコンテキストに追加
          context['member'] = self.get_object()
          return context    

      def test_func(self):
            return self.request.user.is_staff    

    
