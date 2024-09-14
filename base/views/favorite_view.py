from django.urls import reverse_lazy
from django.views.generic import View, ListView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from base.models import Item
from django.http import JsonResponse




class FavoriteListView(LoginRequiredMixin,ListView):
    model = Item
    template_name = 'pages/favorite.html'
    context_object_name = 'favorites'
    paginate_by = 8
    
    def get_queryset(self):
        return self.request.user.favorite_items.all()
      
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_favorites = self.request.user.favorite_items.all()   
        
        for item in context['favorites']:
            item.is_favorite = item in user_favorites
        
        return context
    
    
    
class ToggleFavoriteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        item_id = request.POST.get('item_id')
        item = get_object_or_404(Item, id=item_id)
        user = request.user

        if user.favorite_items.filter(id=item_id).exists():
            user.favorite_items.remove(item)
            is_favorite = False
        else:
            user.favorite_items.add(item)
            is_favorite = True
        
        return JsonResponse({'is_favorite': is_favorite})
    