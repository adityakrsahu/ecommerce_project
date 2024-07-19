from django.shortcuts import render
from .serializers import *

# Create your views here.

def home(request):
    return render (request, 'app/home.html')

def mobile(request):
 return render(request, 'app/mobile.html')


def profile(request):
 return render(request, 'app/profile.html')


def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')