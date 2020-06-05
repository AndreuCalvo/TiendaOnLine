from django.db import models

# Create your models here.
class Client(models.Model):
    name=models.CharField(max_length=30)
    direction=models.CharField(max_length=50)
    telephone=models.CharField(max_length=7)
    email=models.EmailField()

class Article(models.Model):
    name=models.CharField(max_length=30)
    section=models.CharField(max_length=40)
    price=models.IntegerField()

class Order(models.Model):
    number=models.IntegerField()
    date=models.DateField()
    delivered=models.BooleanField()
