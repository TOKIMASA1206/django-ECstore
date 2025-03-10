from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

User = get_user_model()

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = RichTextUploadingField(verbose_name='content')
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    featured_image = models.ImageField(
    upload_to='blog/featured/', 
    blank=True, 
    null=True,
    help_text="記事のメイン画像をアップロード"
    )

    def save(self, *args, **kwargs):
        # 新しいslugを生成
        new_slug = slugify(self.title, allow_unicode=True)
        
        # 編集時の場合（レコードが既に存在する場合）
        if self.pk:
            old = BlogPost.objects.get(pk=self.pk)
            if old.title == self.title:
                new_slug = old.slug

        # ユニーク性のためのチェック（自分自身を除外）
        original_slug = new_slug
        counter = 1
        while BlogPost.objects.filter(slug=new_slug).exclude(pk=self.pk).exists():
            new_slug = f"{original_slug}-{counter}"
            counter += 1

        self.slug = new_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
