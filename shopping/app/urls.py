from django.urls import path
from .views import *

urlpatterns = [
    path("",ProductView.as_view(),name='home'),

    path('product-detail/<int:pk>', ProductDetailView.as_view(), name='product-detail'),

    path('cart/', add_to_cart, name='add-to-cart'),

    path('buy/', buy_now, name='buy-now'),

    path('mobile/', mobile, name='mobile'),
    path('mobile/<slug:data>/', mobile, name='mobiledata'),


    path('laptop/', laptop, name='laptop'),
    path('laaptop/<slug:data>/', laptop, name='laptopdata'),

    path('topwear/', topwear, name='topwear'),
    path('topwear/<slug:data>/', topwear, name='topweardata'),

    path('bottomwear/',bottomwear, name='bottomwear'),
    path('bottomwear/<slug:data>/', bottomwear, name='bottomweardata'),

    path('profile/',profile, name='profile'),
    path('address/', address, name='address'),
    path('orders/', orders, name='orders'),
    path('changepassword/',change_password, name='changepassword'),
    path('login/', login, name='login'),
    path('registration/', CustomerRegistrationView.as_view(), name='customerregistration'),




]