from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name='home'),
    path('mobile/',mobile, name='mobile'),
    path('profile/',profile, name='profile'),
    path('address/', address, name='address'),
    path('orders/', orders, name='orders'),
    path('changepassword/',change_password, name='changepassword'),




]