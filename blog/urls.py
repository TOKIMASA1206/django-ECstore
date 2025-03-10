from django.urls import path, include
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    AdminBlogListView,
    AdminBlogDetailView,
)

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # お客様側の公開ページ
    path('list/', BlogListView.as_view(), name='blog_list'),
    path('post/<str:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    
    # 店舗サイドの管理用ページ
    path('store/list/', AdminBlogListView.as_view(), name='blog_store_list'),
    path('store/post/<str:slug>/', AdminBlogDetailView.as_view(), name='blog_store_detail'),
    path('store/add/', BlogCreateView.as_view(), name='blog_add'),
    path('store/edit/<str:slug>/', BlogUpdateView.as_view(), name='blog_edit'),
    path('store/delete/<str:slug>/', BlogDeleteView.as_view(), name='blog_delete'),
]
