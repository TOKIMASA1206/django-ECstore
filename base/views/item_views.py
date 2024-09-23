from django.shortcuts import render
from django.views.generic import ListView, DetailView
from base.models import Item, Category, Tag
from django.contrib.auth.mixins import LoginRequiredMixin

class ItemSearchView(LoginRequiredMixin,ListView):
    model = Item 
    template_name = 'pages/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q') 
        if query:
            return Item.objects.search(query=query) 
        return Item.objects.filter(is_published=True)
    
    
class IndexListView(ListView):
    model = Item
    template_name = "pages/index.html"
    queryset = Item.objects.filter(is_published=True).order_by('-created_at')


class ItemDetailView(DetailView):
    model = Item
    template_name = "pages/item.html"


class CategoryListView(ListView):
    model = Item
    template_name = "pages/list.html"
    paginate_by = 8

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs["pk"])
        return Item.objects.filter(is_published=True, category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"{self.category.name}"
        context['category_slug'] = self.category.slug
        return context
    
    
class AllItemListView(ListView):
    model = Item
    template_name = "pages/all_item.html"
    paginate_by = 8



class TagListView(ListView):
    model = Item
    template_name = "pages/list.html"
    paginate_by = 8

    def get_queryset(self):
        self.tag = Tag.objects.get(slug=self.kwargs["pk"])
        return Item.objects.filter(is_published=True, tags=self.tag)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"#{self.tag.name}"
        context['tag_slug'] = self.tag.slug

        return context
