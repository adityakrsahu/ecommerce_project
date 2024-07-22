from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from .forms import *

urlpatterns = [
    path("", ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart/', add_to_cart, name='add-to-cart'),
    path('buy/', buy_now, name='buy-now'),
    path('mobile/', mobile, name='mobile'),
    path('mobile/<slug:data>/', mobile, name='mobiledata'),
    path('laptop/', laptop, name='laptop'),
    path('laptop/<slug:data>/', laptop, name='laptopdata'),
    path('topwear/', topwear, name='topwear'),
    path('topwear/<slug:data>/', topwear, name='topweardata'),
    path('bottomwear/', bottomwear, name='bottomwear'),
    path('bottomwear/<slug:data>/', bottomwear, name='bottomweardata'),
    path('profile/', profile, name='profile'),
    path('address/', address, name='address'),
    path('orders/', orders, name='orders'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(
        template_name='app/PasswordChange.html', 
        form_class=PasswordChangeForm, 
        success_url='/passwordchangedone/'
    ), name='changepassword'),
    path("passwordchangedone/", auth_views.PasswordChangeDoneView.as_view(
        template_name='app/passwordchangedone.html'
    ), name="passwordchangedone"),
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='app/login.html', 
        authentication_form=LoginForm
    ), name='login'),
    path('registration/', CustomerRegistrationView.as_view(), name='customerregistration'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
