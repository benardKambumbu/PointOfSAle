from django.contrib import admin
from .models import BkUser, verify_email

admin.site.register(BkUser);
admin.site.register(verify_email);