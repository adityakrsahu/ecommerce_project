from django.shortcuts import render, redirect
# from .serializers import *
from django.views import View
from .models import *
from .forms import  *
from django.contrib import messages



# Create your views here.

# def home(request):
#     return render (request, 'app/home.html')

class ProductView(View):
    def get(self,request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        return render (request, 'app/home.html',
                       {'topwears':topwears,
                        'bottomwears':bottomwears,
                        'mobiles':mobiles, 
                        'laptops':laptops }
                       )


# def product_detail(request):
#  return render(request, 'app/productdetail.html')


class ProductDetailView(View):
  def get(self,request,pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'app/productdetail.html',{'product':product})


def add_to_cart(request, product_id):
    if request.method == 'POST':
        user = request.user
        product = Product.objects.get(id=product_id)  # Fetch the Product instance
        form = CartForm(request.POST)
        
        if form.is_valid():
            cart_item = form.save(commit=False)
            cart_item.user = user
            cart_item.product = product
            cart_item.save()
            return redirect('show_cart')  # Redirect to the cart view
        else:
            # If form is invalid, render the same page with form errors
            data = Cart.objects.filter(user=user)
            return render(request, 'app/addtocart.html', {'form': form, 'data': data})
    else:
        # Handle GET request to display the form
        form = CartForm()
        data = Cart.objects.filter(user=request.user)
        return render(request, 'app/addtocart.html', {'form': form, 'data': data})



def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        print("Cart Items:", cart)  # Debug print
        
        amount = 0.0
        shipping_amount = 80.0
        totalamount = 0.0

        cart_product = [p for p in Cart.objects.all() if p.user == user]
        print("Cart Products:", cart_product)  # Debug print
        
        if cart_product:
            for p in cart_product:
                tempamount = p.quantity * p.product.discounted_price
                amount += tempamount

            totalamount = amount + shipping_amount

        return render(request, 'app/addtocart.html', {'carts': cart, 'totalamount': totalamount, 'amount': amount})
    else:
        return redirect('/login')



def buy_now(request):
 return render(request, 'app/buynow.html')


def mobile(request, data=None):
    if data == None:
        mobiles = Product.objects.filter(category="M")
    elif data == 'Redmi' or data == 'Samsung' or data == 'apple'  or data == 'Phone'or data == 'Android':
        mobiles = Product.objects.filter(category="M").filter(brand=data)
    elif data == 'below':
        mobiles = Product.objects.filter(category="M").filter(discounted_price__lt=10000)    
    elif data == 'above':
        mobiles = Product.objects.filter(category="M").filter(discounted_price__gt=10000) 
    return render(request, 'app/mobile.html',{'mobiles':mobiles})


def laptop(request, data=None):
    if data == None:
        laptops = Product.objects.filter(category="L")
    elif data == 'HP' or data == 'Lenovo' or data == 'Apple' or data == 'ASUS':
        laptops = Product.objects.filter(category="L").filter(brand=data)
    elif data == 'below':
        laptops = Product.objects.filter(category="L").filter(discounted_price__lt=10000)    
    elif data == 'above':
        laptops = Product.objects.filter(category="L").filter(discounted_price__gt=10000) 
    return render(request, 'app/laptop.html',{'laptops':laptops})


def topwear(request, data=None):
    if data == None:
        topwears = Product.objects.filter(category="TW")
    elif data == 'products' or data == 'india':
        topwears = Product.objects.filter(category="TW").filter(brand=data)
    elif data == 'below':
        topwears = Product.objects.filter(category="TW").filter(discounted_price__lt=500)    
    elif data == 'above':
        topwears = Product.objects.filter(category="TW").filter(discounted_price__gt=500) 
    return render(request, 'app/topwear.html',{'topwears':topwears})


def bottomwear(request, data=None):
    if data == None:
        bottomwears = Product.objects.filter(category="BW")
    elif data == 'Roadster' or data == 'Pants' or data == 'india':
       bottomwears = Product.objects.filter(category="BW").filter(brand=data)
    elif data == 'below':
        bottomwears= Product.objects.filter(category="BW").filter(discounted_price__lt=500)    
    elif data == 'above':
        bottomwears = Product.objects.filter(category="BW").filter(discounted_price__gt=500) 
    return render(request, 'app/bottomwear.html',{'bottomwears':bottomwears})



def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'add': add, 'active': 'btn-primary'})


def orders(request):
 return render(request, 'app/orders.html')


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegisterationForm()
        return render(request, 'app/customerregistration.html',{'form':form})
    def post(self , request):
        form = CustomerRegisterationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'congratulations!! Registered Successfully')
            form.save()
        return render(request, 'app/customerregistration.html',{'form':form})


      


class ProfileViewe(View):
    def get(self, request):
        form = CustomberProfileForm()
        return render(request, 'app/profile.html', {'form': form , 'active':'btn-primary'})
    
    def post(self, request):
        form = CustomberProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            # user = form.cleaned_data['user']
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            door_flat_no = form.cleaned_data['door_flat_no']
            phone = form.cleaned_data['phone']
            city = form.cleaned_data['city']
            state= form.cleaned_data['state']
            zip_code= form.cleaned_data['zip_code']
            # image = form.cleaned_data['image']

            reg = Customer(user=user, name= name, address=address,door_flat_no=door_flat_no, phone=phone,city=city, state=state,
                           zip_code=zip_code)
            reg.save()
            messages.success(request, 'Congratulations !! Profile Updated Successfully')


        # return redirect('profile')  # Assuming you have a 'profile' URL name
        return render(request, 'app/profile.html', {'form': form})
    


def checkout(request):
 return render(request, 'app/checkout.html')
   