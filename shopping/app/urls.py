from django.urls import path
from .views import *

urlpatterns = [
    path("",ProductView.as_view(),name='home'),




    path('product-detail/', product_detail, name='product-detail'),



    path('mobile/',mobile, name='mobile'),
    path('profile/',profile, name='profile'),
    path('address/', address, name='address'),
    path('orders/', orders, name='orders'),
    path('changepassword/',change_password, name='changepassword'),
    path('login/', login, name='login'),
    path('registration/', customerregistration, name='customerregistration'),




]