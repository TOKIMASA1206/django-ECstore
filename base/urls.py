from django.urls import path
from base import views

urlpatterns = [  
    #店舗オーナーサイド
    # =======================  USER =========================
    path('users/', views.AdminUserListView.as_view(), name='store_users'),
    
    # =======================  ITEM =========================
    path('items/', views.AdminItemListView.as_view(), name='store_items'),
    path('items/add/', views.AdminItemCreateView.as_view(), name='store_item_add'),
    path('items/edit/<str:pk>/', views.AdminItemUpdateView.as_view(), name='store_item_edit'),
    path('items/delete/<str:pk>/', views.AdminItemDeleteView.as_view(), name='store_item_delete'),
    
    # =======================  CATEGORY =========================
    
    path('categories/', views.AdminCategoryListView.as_view(), name='store_categories'),
    path('categories/add/', views.AdminCategoryCreateView.as_view(), name='store_category_add'),
    path('categories/edit/<slug:slug>/', views.AdminCategoryUpdateView.as_view(), name='store_category_edit'),
    path('categories/delete/<slug:slug>/', views.AdminCategoryDeleteView.as_view(), name='store_category_delete'),
    
    # =======================  TAG =============================
    
    
    path('tags/', views.AdminTagListView.as_view(), name='store_tags'),
    path('tags/add/', views.AdminTagCreateView.as_view(), name='store_tag_add'),
    path('tags/edit/<slug:slug>/', views.AdminTagUpdateView.as_view(), name='store_tag_edit'),
    path('tags/delete/<slug:slug>/', views.AdminTagDeleteView.as_view(), name='store_tag_delete'),
    
    # =======================  ORDER =============================
    
    path('orders/', views.AdminOrderListView.as_view(), name='store_orders'),
    
    # =======================  ABOUT =============================
    
    path('about/', views.AboutStoreListView.as_view(), name='store_about'),
    path('about/<int:pk>/edit/', views.AboutStoreUpdateView.as_view(), name='store_about_edit'),
    path('members/', views.MemberListView.as_view(), name='store_members'),
    path('members/add/', views.MemberCreateView.as_view(), name='store_member_add'),
    path('members/<int:pk>/edit/', views.MemberUpdateView.as_view(), name='store_member_edit'),
    path('members/<int:pk>/delete/', views.MemberDeleteView.as_view(), name='store_member_delete'),
]