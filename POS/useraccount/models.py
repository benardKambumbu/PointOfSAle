

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from PIL import Image
from django.conf import settings
from django.contrib.auth.models import User
import os

# Create your models here.

# def user_directory_path(instance,filename):

# 	profile_pic_name = 'user_{0}/profile.jpg'.format(instance.user.id)
# 	full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

# 	if os.path.exists(full_path):
# 		os.remove(full_path)

class BkUser(models.Model):
	bkuser = models.ForeignKey(User, on_delete=models.CASCADE)
	profile_image= models.ImageField(null=True, blank=True,upload_to="UserAccount/profile_image")
	shop = models.CharField(max_length = 255,null=True, blank=True)
	position = models.CharField(max_length = 255,null=True, blank=True)
	creation_date = models.DateField(auto_now_add=True)
	address = models.CharField(max_length = 255)
	phoneNo = models.CharField(max_length = 255)
	whatsapp = models.CharField(max_length = 255,null=True, blank=True)
	

	# def save(self, *args, **kwargs):
	# 	super().save(*args, **kwargs)
	# 	if self.profile_image:
	# 		img = Image.open(self.profile_image.path)

	# 		if img.height > 300  or img.width >300:
	# 			output_size = (300,300)
	# 			img.thumbnail(output_size)
	# 			img.save(self.profile_image.path)

class verify_email(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	email= models.TextField(blank=True,null=True)
	verification_code = models.TextField(blank=True,null=True)