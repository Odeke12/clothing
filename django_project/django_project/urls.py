"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf 
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  
from django.contrib.auth import views as auth_views 
from django.urls import path, include
from users import views as user_views  
from shop import views as shop_views
from customers import views as cust_views
from django.conf import settings  
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('register/', user_views.register, name='register'), 
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name='logout'),
    path('login-shop/', auth_views.LoginView.as_view(template_name="customers/login.html"), name='login-shop'),
    path('logout-shop/', auth_views.LogoutView.as_view(template_name="customers/logout.html"), name='logout-shop'),
   #shop urls start here
   path('shop-search/', shop_views.search, name='search'),
    path('shop-cart/', shop_views.CartListView.as_view(), name='shop-cart'),
    path('', shop_views.HomeListView.as_view(), name='shop-home'),
    path('profile/', user_views.profile, name='profile'),
    path('shop-category/', shop_views.CategoryListView.as_view(), name='shop-category'),
    path('shop-male/', shop_views.men, name='shop-male'),
    path('shop-shoes/', shop_views.shoes, name='shop-shoes'),
    path('shop-female/', shop_views.women, name='shop-female'),
    path('item/<slug>/',  shop_views.ItemDetailView.as_view(), name='item-detail'),
    #path('item/<slug>/',  shop_views.ItemDetail, name='item-detail'),
    path('add-to-cart/<slug>', shop_views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>', shop_views.remove_from_cart,name='remove-from-cart'),
    path('remove-single-item-from-cart/<slug>', shop_views.remove_single_item_from_cart,name='remove-single-item-from-cart'),
    path('shop-checkout/', shop_views.Checkout.as_view(), name='shop-checkout'),
    path('payment/<payment_option>',shop_views.PaymentView.as_view(), name='payment'),
    #shop urls end here
    #customer urls start here
    path('shop-registration/', cust_views.register, name='shop-registration'),
    path('shop-profile/', cust_views.shop_profile, name='shop-profile'),
    #blog urls
    path('', include('blog.urls')),  
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


