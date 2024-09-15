from base.forms import UserCreationForm
from django.contrib import admin
from base.models import Item, Category, Tag, User, Profile, Order, Image
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
 
 
class TagInline(admin.TabularInline):
    model = Item.tags.through
    
class ImageInline(admin.TabularInline):
    model = Image
    extra = 1  
 
 
class ItemAdmin(admin.ModelAdmin):
    inlines = [TagInline, ImageInline]
    exclude = ['tags']
 
 
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
 
 
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password',)}),
        (None, {'fields': ('is_active', 'is_admin',)}),
    )
 
    list_display = ('username', 'email', 'is_active',)
    list_filter = ()
    ordering = ()
    filter_horizontal = ()
 
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'is_active',)}),
    )
 
    add_form = UserCreationForm
 
    inlines = (ProfileInline,)
 
 
admin.site.register(Order)
admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
