from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class Castomer(models.Model):
    # 

class Castomer(models.Model):
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


class Pr
