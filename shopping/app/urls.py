from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name='home'),
    path('mobile/',mobile, name='mobile'),
    path('profile/',profile, name='profile'),
    path('address/', address, name='address'),



]