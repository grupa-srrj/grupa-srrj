from django.db import models

class Cars (models.Model):
    brand = models.CharField(max_length= 32)
    engine_type = models.CharField(max_length= 32)
    engine_capacity = models.CharField(max_length= 32)
    engine_power = models.CharField(max_length= 32)
    image= models.ImageField(upload_to='cars/obrazki')
    is_available = models.BooleanField(default=True)


    added = models.DateTimeField(auto_now_add=True)



class Customer (models.Model):
    name = models.CharField(max_length= 64)
    address = models.CharField(max_length= 32)
    phone_number = models.CharField(max_length= 32)

    added = models.DateTimeField(auto_now_add=True)



