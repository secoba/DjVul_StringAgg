# Create your models here.


from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
