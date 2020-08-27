from django.db import models

from django.utils import timezone
import json

from django.conf import settings
from django.utils.translation import ugettext, ugettext_lazy as _

from six import python_2_unicode_compatible
# Create your models here.

class Categoryy(models.Model):
    id = models.IntegerField(primary_key=True)
    categoryname = models.CharField(max_length=200)
    categorydescription = models.CharField(max_length=200,blank=True)
    categoryimg =models.CharField(max_length=300,blank=True)
    def __str__(self):
        return self.categoryname

class Product(models.Model):
    id = models.CharField(max_length=200,primary_key=True)
    category = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    domain = models.CharField(max_length=200,blank=True)
    name = models.TextField(null=True,blank=True)
    reference = models.CharField(max_length=200,blank=True)
    discount = models.CharField(max_length=200,blank=True)
    url = models.CharField(max_length=200,blank=True)
    timestamp = models.DateTimeField(blank=True)
    brand = models.CharField(max_length=200,blank=True)
    priceString = models.CharField(max_length=200,blank=True)
    retailer = models.CharField(max_length=200,blank=True)
    marketplace = models.CharField(max_length=200,blank=True)
    seller = models.CharField(max_length=200,blank=True)
    price = models.FloatField(blank=True)
    currency= models.CharField(max_length=200,blank=True)
    sub_category = models.CharField(max_length=200,blank=True)
    country = models.CharField(max_length=200,blank=True)
    short_description = models.TextField(null=True,blank=True)
    old_price = models.FloatField(blank=True)
    image = models.CharField(max_length=200,blank=True)
    marketplaceId = models.CharField(max_length=200,blank=True)
    categorymap = models.ForeignKey(Categoryy, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name