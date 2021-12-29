from types import CodeType
from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    stock=models.IntegerField()
    image_url=models.CharField(max_length=2083)


class Offer(models.Model):
    code=models.CharField(max_length=10)
    description=models.CharField(max_length=255)
    discount=models.FloatField()