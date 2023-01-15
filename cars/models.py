from django.db import models

class Cars (models.Model):
    brande = models.CharField(max_length= 32)
    engine_type = models.CharField(max_length= 32)
    engine_capasity = models.CharField(max_length= 32)
    engine_power = models.CharField(max_length= 32)
    is_available = models.BooleanField(default=True)


    added = models.DateTimeField(auto_now_add=True)



class Customer (models.Model):
    name = models.CharField(max_length= 64)
    adress = models.CharField(max_length= 32)
    phone_number = models.CharField(max_length= 32)

    added = models.DateTimeField(auto_now_add=True)



