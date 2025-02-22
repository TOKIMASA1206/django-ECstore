from django.contrib import admin
from django.urls import path
from base import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

# カスタム404ハンドラーの追加
from django.conf.urls import handler404
handler404 = views.custom_404

urlpatterns = [
    path("admin/", admin.site.urls),
    
    #店舗オーナーサイド
    # =======================  USER =========================
    path('store/users/', views.AdminUserListView.as_view(), name='store_users'),
    
    # =======================  ITEM =========================
    path('store/items/', views.AdminItemListView.as_view(), name='store_items'),
    path('store/items/add/', views.AdminItemCreateView.as_view(), name='store_item_add'),
    path('store/items/edit/<str:pk>/', views.AdminItemUpdateView.as_view(), name='store_item_edit'),
    path('store/items/delete/<str:pk>/', views.AdminItemDeleteView.as_view(), name='store_item_delete'),
    
    # =======================  CATEGORY =========================
    
    path('store/categories/', views.AdminCategoryListView.as_view(), name='store_categories'),
    path('store/categories/add/', views.AdminCategoryCreateView.as_view(), name='store_category_add'),
    path('store/categories/edit/<slug:slug>/', views.AdminCategoryUpdateView.as_view(), name='store_category_edit'),
    path('store/categories/delete/<slug:slug>/', views.AdminCategoryDeleteView.as_view(), name='store_category_delete'),
    
    # =======================  TAG =============================
    
    
    path('store/tags/', views.AdminTagListView.as_view(), name='store_tags'),
    path('store/tags/add/', views.AdminTagCreateView.as_view(), name='store_tag_add'),
    path('store/tags/edit/<slug:slug>/', views.AdminTagUpdateView.as_view(), name='store_tag_edit'),
    path('store/tags/delete/<slug:slug>/', views.AdminTagDeleteView.as_view(), name='store_tag_delete'),
    
    # =======================  ORDER =============================
    
    path('store/orders/', views.AdminOrderListView.as_view(), name='store_orders'),
    
    
    
    
    # Account
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("account/", views.AccountUpdateView.as_view(), name="account_update"),
    path("profile/", views.ProfileUpdateView.as_view(), name="profile_update"),
    # Contact
    path("contact/", views.ContactFormView.as_view(), name="contact"),
    path("contact/result/", views.ContactResultView.as_view(), name="contact_result"),
    path(
        "contact/failure/", views.ContactFailureView.as_view(), name="contact_failure"
    ),
    # Order
    path("orders/<str:pk>/", views.OrderDetailView.as_view(), name="order_detail"),
    path("orders/", views.OrderIndexView.as_view(), name="order_index"),
    # Pay
    path("pay/checkout/", views.PayWithStripe.as_view(), name="pay_checkout"),
    path("pay/success/", views.PaySuccessView.as_view(), name="pay_success"),
    path("pay/cancel/", views.PayCancelView.as_view(), name="pay_cancel"),
    # Cart
    path("cart/remove/<str:pk>/", views.remove_from_cart, name="remove_from_cart"),
    path("cart/add/", views.AddCartView.as_view(), name="add_to_cart"),
    path("cart/", views.CartListView.as_view(), name="cart_list"),
    # Favorite
    path(
        "item/<str:pk>/toggle_favorite/",
        views.ToggleFavoriteView.as_view(),
        name="toggle_favorite",
    ),
    path("favorites/", views.FavoriteListView.as_view(), name="favorite_list"),
    # About
    path("about/", views.AboutIndexView.as_view(), name="about"),
    # Search
    path("search/", views.ItemSearchView.as_view(), name="item_search"),
    # Items
    path("items/<str:pk>/", views.ItemDetailView.as_view(), name="item_detail"),
    path(
        "categories/<str:pk>/", views.CategoryListView.as_view(), name="category_detail"
    ),
    path("all/items/", views.AllItemListView.as_view(), name="all_items"),
    path("tags/<str:pk>/", views.TagListView.as_view(), name="tag_detail"),
    path("", views.IndexListView.as_view()),  # トップページ
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

