from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField

class About(models.Model):
    # header_image = models.ImageField(upload_to='about/header/', blank=True, null=True)
    header_image = CloudinaryField('header image', folder='about/header', blank=True, null=True)
    store_description = models.TextField(blank=True, null=True)
    team_comment = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "AboutPage"
      
User = get_user_model()

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member')
    # profile_image = models.ImageField(upload_to='about/members/', blank=True, null=True)
    profile_image = CloudinaryField('profile image', folder='about/members', blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} のメンバー情報" 
      
  
      
      