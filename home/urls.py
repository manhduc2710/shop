from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('cart', views.cart, name='cart'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('register', views.register, name='register'),
    path('checkout', views.checkout, name='checkout'),
    path('login/',views.loginpage, name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
    path('detail/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('category/', views.category, name='category'),
    path('update_item/', views.updateItem, name='update_item'),
    path('add-to-cart', views.addtocart, name="addtocart")
]