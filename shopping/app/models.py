from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    door_flat_no = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=10)
    image = models.ImageField(upload_to='profile_images/')

    def __str__(self):
        return self.name
