from django import forms
from importlib import import_module
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
import random
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import string
from django.urls import reverse_lazy, reverse
from django.db.models import Avg, Count, Min, Sum
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *




class ShopForm(forms.ModelForm):
	class Meta:
		model = Shop
		fields = ('shop_name','shop_category','shop_moto','shop_bio',
			'phoneNo','phoneNo_2','address','email','whatsapp')
		widgets = {
		'shop_name': forms.TextInput(attrs={'class':'form-control','placeholder':'unique, max-length:50 char'}),
		'shop_moto': forms.TextInput(attrs={'class':'form-control','placeholder':'less than 30 words '}),
		'shop_logo': forms.FileInput(attrs={'class':'form-control','placeholder':'less than 30 words '}),
		'shop_trademark': forms.FileInput(attrs={'class':'form-control'}),
		'shop_bio': forms.Textarea(attrs={'class':'form-control','placeholder':'less than 500 words '}),
		'shop_title_tag': forms.TextInput(attrs={'class':'form-control','placeholder':'shop webpage title'}),
		'shop_category': forms.Select(choices=( ("",""), ("Fashion_&_Beauty","Fashion_&_Beauty"),("Kids & Babies","Kids & Babies"),
			("Teenage & Early 20's","Teenage & Early 20's"),("Men & Women","Men & Women"),
			("Gadgets & Accessories","Gadgets & Accessories"),("Electronics & Accessories","Electronics & Accessories"),
			("Groceries","Groceries"),("Hardware","Hardware"),) ,attrs={'class':'form-control','placeholder':'important for searchies'}),
		'phoneNo': forms.TextInput(attrs={'class':'form-control','placeholder':'required '}),
		'phoneNo_2': forms.TextInput(attrs={'class':'form-control','placeholder':'reccomended'}),
		'phoneNo_3': forms.TextInput(attrs={'class':'form-control','placeholder':'optional'}),
		'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'should be verifiable'}),
		'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'verification will be sent'}),
		'whatsapp': forms.TextInput(attrs={'class':'form-control', 'placeholder':'recomended '}),
		'whatsapp_2': forms.TextInput(attrs={'class':'form-control', 'placeholder':'optional '}),
		'facebook': forms.TextInput(attrs={'class':'form-control', 'placeholder':'recomended'}),
		'profile': forms.FileInput(attrs={'class':'form-control'}),
		
		}






	
class ProductForm(forms.ModelForm):

	
		
	class Meta:
		model = Product
		fields = ('product_name','product_description','product_price',
			'product_promotion','product_promote','product_specifications')	
		widgets = {
		'product_name': forms.TextInput(attrs={'class':'form-control'}),
		'product_price': forms.TextInput(attrs={'class':'form-control'}),
		'product_description': forms.Textarea(attrs={'class':'form-control'}),
		'product_promotion': forms.TextInput(attrs={'class':'form-control'}),

		'product_category': forms.Select(choices=(  ("payments","payments"),("payments","payments",)) ,attrs={'class':'form-control'}),
		
		'product_specifications': forms.Textarea(attrs={'class':'form-control'}),
		'product_tag': forms.TextInput(attrs={'class':'form-control'}),
		'product_main_image': forms.FileInput(attrs={'class':'form-control'}),
		'product_image1': forms.FileInput(attrs={'class':'form-control'}),
		'product_image2': forms.FileInput(attrs={'class':'form-control'}),
		'product_image3': forms.FileInput(attrs={'class':'form-control'}),
		'product_image4': forms.FileInput(attrs={'class':'form-control'}),
		'product_image5': forms.FileInput(attrs={'class':'form-control'}),
		'product_color1': forms.TextInput(attrs={'class':'form-control'}),
		'product_color2': forms.TextInput(attrs={'class':'form-control'}),
		'product_color3': forms.TextInput(attrs={'class':'form-control'}),
		'product_color4': forms.TextInput(attrs={'class':'form-control'}),
		'product_color5': forms.TextInput(attrs={'class':'form-control'}),
		'product_size1': forms.TextInput(attrs={'class':'form-control'}),
		'product_size2': forms.TextInput(attrs={'class':'form-control'}),
		'product_size3': forms.TextInput(attrs={'class':'form-control'}),
		'product_size4': forms.TextInput(attrs={'class':'form-control'}),
		'product_size5': forms.TextInput(attrs={'class':'form-control'}),
		'product_promote':forms.CheckboxInput(attrs={'class':'form-check-input', 'type': 'checkbox',  'id':'flexCheckChecked'}),
	
	
		}


