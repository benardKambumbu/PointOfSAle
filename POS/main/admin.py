from django.contrib import admin
from .models import *

admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CheckedOut)
admin.site.register(Transactions)