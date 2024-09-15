from django.conf import settings
from base.models import Item, Category,Tag
 
 
def base(request):
    items = Item.objects.filter(is_published=True)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return {
        'TITLE': settings.TITLE,
        'ADDTIONAL_ITEMS': items,
        'POPULAR_ITEMS': items.order_by('-sold_count'),
        'CATEGORY_ITEMS':categories,
        'TAG_ITEMS':tags
    }
