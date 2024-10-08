from django.contrib import admin
from django.urls import path
from base import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
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

