from django.db import models
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
import os
from django.db.models import Q

#Search
class ItemModelQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        qs = qs.filter(is_published=True)
        if query is not None:
            or_lookup = (
                Q(name__icontains=query)|
                Q(description__icontains=query)
            )
            qs = qs.filter(or_lookup).distinct()
        return qs.order_by("-created_at")    


class ItemModelManager(models.Manager):
    def get_queryset(self):
        return ItemModelQuerySet(self.model, using=self.db)
    
    def search(self, query=None):
        return self.get_queryset().search(query=query)


# IDをランダムに決定
def create_id():
    return get_random_string(22)


# # 画像のURLを保存
def upload_image_to(instance, filename):

    item_id = str(instance.item.id)
    return os.path.join('items', item_id, filename) 




# Tagのクラス
class Tag(models.Model):
    slug = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Categoryのクラス
class Category(models.Model):
    slug = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Imageのクラス
class Image(models.Model):
    image = models.ImageField(default="", blank=True, upload_to=upload_image_to)
    item = models.ForeignKey(
    'Item', 
    on_delete=models.CASCADE, 
    related_name='images', 
    null=True, 
    blank=True
)
    
    def __str__(self):
        return self.image.name

class Item(models.Model):
    id = models.CharField(
        default=create_id, primary_key=True, max_length=22, editable=False
    )
    name = models.CharField(default="", max_length=50)
    price = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    description = models.TextField(default="", blank=True)
    sold_count = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = ItemModelManager()
    
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True
    )

    # ManyToManyでつなげる  中間テーブルが存在する
    tags = models.ManyToManyField(Tag)

    # adminで管理する際にオブジェクトの識別が容易になります
    def __str__(self):
        return self.name



