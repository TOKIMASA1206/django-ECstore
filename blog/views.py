# blog/views.py
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from .forms import BlogPostForm

# 公開用ビュー
class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(published=True).order_by('-created_at')

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'
    
    
    
    
# 管理用（店舗サイド）のブログ記事作成ビュー
    
    
class AdminBlogListView(LoginRequiredMixin, UserPassesTestMixin,ListView):
    model = BlogPost
    template_name = 'store/blog_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(published=True).order_by('-created_at')
      
    def test_func(self):
        return self.request.user.is_staff   

class AdminBlogDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = BlogPost
    template_name = 'store/blog_detail.html'
    context_object_name = 'post'
    
    def test_func(self):
        return self.request.user.is_staff 


class BlogCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'store/blog_form.html'
    success_url = reverse_lazy('blog_store_list')

    def test_func(self):
        return self.request.user.is_staff  # スタッフのみアクセス可能

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# 更新ビュー
class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'store/blog_form.html'
    success_url = reverse_lazy('blog_store_list')

    def test_func(self):
        return self.request.user.is_staff

# 削除ビュー
class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    template_name = 'store/blog_confirm_delete.html'
    success_url = reverse_lazy('blog_store_list')

    def test_func(self):
        return self.request.user.is_staff
