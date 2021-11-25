from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from PIL import Image
from django.conf import settings
from django.contrib.auth.models import User
import os

# Create your models here.
class Shop(models.Model):
	
	shop_name = models.CharField(max_length = 255)
	shop_moto = models.CharField(max_length = 255)
	shop_bio = models.TextField(blank=True,null=True)
	shop_category = models.CharField(max_length = 255)
	phoneNo = models.CharField(max_length = 255)
	phoneNo_2 = models.CharField(max_length = 255,null=True, blank=True)
	address = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	whatsapp = models.CharField(max_length = 255,null=True, blank=True)
	
	

class Product(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	shop_name = models.ForeignKey(Shop, on_delete=models.CASCADE)
	product_name= models.CharField(max_length = 255)
	product_description = models.TextField(blank=True,null=True)
	product_model = models.CharField(max_length = 255,null=True, blank=True,)
	product_part_number = models.CharField(max_length = 255,null=True, blank=True,)
	product_price= models.CharField(max_length = 255)
	product_promote = models.BooleanField( blank=True,null=True,default=False)
	product_promotion= models.CharField(max_length = 255,null=True, blank=True,)
	product_size= models.CharField(max_length = 225,null=True, blank=True,)
	product_quantity= models.IntegerField(default=1)
	product_creation_date = models.DateField(auto_now_add=True)
	product_specifications= models.TextField(null=True, blank=True, )
	product_last_price = models.CharField(max_length = 225,null=True, blank=True, )

class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	customer = models.TextField(blank=True,null=True)
	shop_name = models.ForeignKey(Shop, on_delete=models.CASCADE)
	product_name= models.CharField(max_length = 255)
	product_description = models.TextField(blank=True,null=True)
	product_model = models.CharField(max_length = 255,null=True, blank=True,)
	product_part_number = models.CharField(max_length = 255,null=True, blank=True,)
	product_price= models.CharField(max_length = 255)
	product_promote = models.BooleanField( blank=True,null=True,default=False)
	product_promotion= models.CharField(max_length = 255,null=True, blank=True,)
	product_size= models.CharField(max_length = 225,null=True, blank=True,)
	product_quantity= models.IntegerField(default=1)
	product_creation_date = models.DateField(auto_now_add=True)
	product_specifications= models.TextField(null=True, blank=True, )
	product_last_price = models.CharField(max_length = 225,null=True, blank=True, )

class CheckedOut(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	code = models.TextField(blank=True,null=True)
	customer = models.TextField(blank=True,null=True)
	shop_name = models.ForeignKey(Shop, on_delete=models.CASCADE)
	product_name= models.CharField(max_length = 255)
	product_description = models.TextField(blank=True,null=True)
	product_model = models.CharField(max_length = 255,null=True, blank=True,)
	product_part_number = models.CharField(max_length = 255,null=True, blank=True,)
	product_price= models.CharField(max_length = 255)
	product_promote = models.BooleanField( blank=True,null=True,default=False)
	product_promotion= models.CharField(max_length = 255,null=True, blank=True,)
	product_size= models.CharField(max_length = 225,null=True, blank=True,)
	product_quantity= models.IntegerField(default=1)
	product_creation_date = models.DateTimeField(auto_now_add=True)
	product_specifications= models.TextField(null=True, blank=True, )
	product_last_price = models.CharField(max_length = 225,null=True, blank=True, )
	product_buying_price = models.CharField(max_length = 225,null=True, blank=True, )
	total = models.CharField(max_length = 225,null=True, blank=True,)

class Transactions(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	code = models.TextField(blank=True,null=True)
	customer = models.TextField(blank=True,null=True)
	shop_name = models.ForeignKey(Shop, on_delete=models.CASCADE)
	products= models.TextField(max_length = 255)
	product_description = models.TextField(blank=True,null=True)
	paymentMethod = models.CharField(max_length = 225,null=True, blank=True, )
	date= models.DateTimeField(auto_now_add=True)
	total= models.TextField(null=True, blank=True, )
	
	


