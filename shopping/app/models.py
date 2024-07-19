from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class Castomer(models.Model):
    # 

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    door_flat_no = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=10)
    image = models.ImageField(upload_to='profile_images/')

    def __str__(self):
        return str(self.id)
    

CATEGORY_CHOICES = (
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('TW','Top Wear'),
    ('BW','Botton Wear'),
)


class Product(models.Model):
    titel=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='productimg')

    def __str__(self) -> str:
        return str(self.id)
    
class Cart(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return str(self.id)
    

STATUSE_CHOICES =(
('Accepted','Acceptted'),
('packed','packed'),
('On The Way','On The Way'),
('Delivered','Delivered'),
('cancel','Cancal')

)


class OrderPlaced(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)
    order_date= models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUSE_CHOICES,default='pending')

