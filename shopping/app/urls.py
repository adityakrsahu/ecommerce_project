from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from .forms import *

urlpatterns = [
    path("", ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add-to-cart'),
    path('cart/', show_cart, name='showcart'),


    path('buy/', buy_now, name='buy-now'),
    path('mobile/', mobile, name='mobile'),
    path('mobile/<slug:data>/', mobile, name='mobiledata'),
    path('laptop/', laptop, name='laptop'),
    path('laptop/<slug:data>/', laptop, name='laptopdata'),
    path('topwear/', topwear, name='topwear'),
    path('topwear/<slug:data>/', topwear, name='topweardata'),
    path('bottomwear/', bottomwear, name='bottomwear'),
    path('bottomwear/<slug:data>/', bottomwear, name='bottomweardata'),

    path('profile/', ProfileViewe.as_view(), name='profile'),

    path('address/', address, name='address'),
    path('orders/', orders, name='orders'),


    # =========== forget password =================


     path('changepassword/', auth_views.PasswordChangeView.as_view(
        template_name='app/password_change.html', 
        form_class=PasswordChangeForm, 
        success_url='/passwordchangedone/'
    ), name='changepassword'),

    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(
        template_name='app/password_change_done.html'
    ), name='passwordchangedone'),

    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='app/password_reset.html', 
        form_class=PasswordResetForm
    ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='app/password_reset_done.html'
    ), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='app/password_reset_confirm.html',
        form_class=SetPasswordForm
    ), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='app/password_reset_complete.html'
    ), name='password_reset_complete'),

    # ===================== end forget password ==============.

    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='app/login.html', 
        authentication_form=LoginForm
    ), name='login'),
    path('registration/', CustomerRegistrationView.as_view(), name='customerregistration'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('checkout/', checkout, name='checkout'),
]


