from django.db import models
from django.utils.crypto import get_random_string
import os

# IDをランダムに決定
def create_id():
  return get_random_string(22)
# 画像のURLを保存
def upload_image_to(instance, filename):
  item_id = instance.id
  return os.path.join('static', 'items',item_id, filename)



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


class Item(models.Model):
    id = models.CharField(default=create_id, primary_key=True, max_length=22, editable=False)
    name = models.CharField(default='', max_length=50)
    price = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    description = models.TextField(default= '', blank=True)
    sold_count = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(default="", blank=True, upload_to=upload_image_to)
    
    
    # ForeignKeyでつなげる
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)
    
    # ManyToManyでつなげる  中間テーブルが存在する
    tags = models.ManyToManyField(Tag)

    # adminで管理する際にオブジェクトの識別が容易になります
    def __str__(self):
        return self.name
    