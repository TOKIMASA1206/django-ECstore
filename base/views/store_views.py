# views.py
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from base.models import Item, User,Category,Tag,Order
from django.shortcuts import redirect
from base.forms import ItemForm, ImageFormSet, CategoryForm, TagForm
from django.utils.text import slugify
import logging

logger = logging.getLogger(__name__)


# ===============================  USER  ==========================

class AdminUserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = 'store/pages/users/index.html'
    context_object_name = 'users'
    paginate_by = 10 
    
    def test_func(self):
        return self.request.user.is_staff    
    
# =========================  ITEM  ================================= 
    
class AdminItemListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Item
    form_class = ItemForm 
    template_name = 'store/pages/items/index.html'
    context_object_name = 'items'
    paginate_by = 10
    
    def test_func(self):
        return self.request.user.is_staff 
      

class AdminItemCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'store/pages/items/add.html'
    success_url = reverse_lazy('store_items')

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['image_formset'] = ImageFormSet(self.request.POST, self.request.FILES)
        else:
            data['image_formset'] = ImageFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        image_formset = context['image_formset']
        if image_formset.is_valid():
            self.object = form.save()
            image_formset.instance = self.object
            image_formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))      

logger = logging.getLogger(__name__)

class AdminItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'store/pages/items/edit.html'
    success_url = reverse_lazy('store_items')

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            context['image_formset'] = ImageFormSet(
                self.request.POST, self.request.FILES, instance=self.object
            )
        else:
            context['image_formset'] = ImageFormSet(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        image_formset = ImageFormSet(
            request.POST, request.FILES, instance=self.object
        )
        if form.is_valid() and image_formset.is_valid():
            return self.form_valid(form, image_formset)
        else:
            return self.form_invalid(form, image_formset)

    def form_valid(self, form, image_formset):
        self.object = form.save()
        image_formset.instance = self.object
        image_formset.save()
        return redirect(self.get_success_url())

    def form_invalid(self, form, image_formset):
    # フォームのエラーをログに記録
        if form.errors:
            logger.error("Item form is invalid.")
            logger.error(form.errors)
        
        # 画像フォームセットのエラーをログに記録
        if image_formset.errors:
            logger.error("Image formset is invalid.")
            for form_errors in image_formset.errors:
                logger.error(form_errors)
        
        context = self.get_context_data(form=form)
        context['image_formset'] = image_formset
        return self.render_to_response(context)
        
class AdminItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    template_name = 'store/pages/items/delete.html'
    success_url = reverse_lazy('store_items')

    def test_func(self):
        return self.request.user.is_staff      
    
# ========================  CATEGORY   ======================= 
    
class AdminCategoryListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Category 
    template_name = 'store/pages/categories/index.html'  # テンプレートのパス
    context_object_name = 'categories'
    paginate_by = 10  # ページネーション（1ページあたりの項目数）

    def test_func(self):
        return self.request.user.is_staff  # 管理者のみアクセス可能
    


class AdminCategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Category
    form_class = CategoryForm 
    template_name = 'store/pages/categories/add.html'
    success_url = reverse_lazy('store_categories')

    def test_func(self):
        return self.request.user.is_staff
      
      
      
            
      
class AdminCategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Category
    form_class = CategoryForm 
    template_name = 'store/pages/categories/edit.html'
    success_url = reverse_lazy('store_categories')

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        # 名前が変更された場合、スラッグを自動更新
        if 'name' in form.changed_data:
            form.instance.slug = slugify(form.instance.name)
            # スラッグの一意性を確保
            counter = 1
            unique_slug = form.instance.slug
            while Category.objects.filter(slug=unique_slug).exclude(pk=form.instance.pk).exists():
                unique_slug = f"{form.instance.slug}-{counter}"
                counter += 1
            form.instance.slug = unique_slug
        return super().form_valid(form)


class AdminCategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    template_name = 'store/pages/categories/delete.html'
    success_url = reverse_lazy('store_categories')

    def test_func(self):
        return self.request.user.is_staff      


# =========================  TAG ===================================

class AdminTagListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Tag
    form_class = TagForm 
    template_name = 'store/pages/tags/index.html'  # テンプレートのパス
    context_object_name = 'tags'
    paginate_by = 10  # ページネーション（1ページあたりの項目数）

    def test_func(self):
        return self.request.user.is_staff   
      
      
class AdminTagCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Tag
    form_class = TagForm 
    template_name = 'store/pages/tags/add.html'
    success_url = reverse_lazy('store_tags')

    def test_func(self):
        return self.request.user.is_staff      
      
class AdminTagUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tag
    form_class = TagForm 
    template_name = 'store/pages/tags/edit.html'
    success_url = reverse_lazy('store_tags')

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        # 名前が変更された場合、スラッグを自動更新
        if 'name' in form.changed_data:
            form.instance.slug = slugify(form.instance.name)
            # スラッグの一意性を確保
            counter = 1
            unique_slug = form.instance.slug
            while Tag.objects.filter(slug=unique_slug).exclude(pk=form.instance.pk).exists():
                unique_slug = f"{form.instance.slug}-{counter}"
                counter += 1
            form.instance.slug = unique_slug
        return super().form_valid(form)


class AdminTagDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tag
    template_name = 'store/pages/tags/delete.html'
    success_url = reverse_lazy('store_tags')

    def test_func(self):
        return self.request.user.is_staff      
      
      
# ========================  ORDER  ================================


class AdminOrderListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Order
    template_name = 'store/pages/orders/index.html'
    context_object_name = 'orders'
    paginate_by = 10

    def test_func(self):
        return self.request.user.is_staff
        
