from django.contrib import admin
from django.urls import path
from .views import UserRegister, UserRegister2, bkaccounts, userprofile, UserRegister22
from django.conf.urls import url, include

urlpatterns = [

    path('register/', UserRegister.as_view(), name='register'),
 	path('User_profile/', UserRegister2.as_view(), name='register2'),
  	path('User_profile_admin/', UserRegister22.as_view(), name='register22'),
 	path('bkaccounts/', bkaccounts, name='bkaccounts'),
    url(r'^update_profile/(?P<pk>[0-9]+)/$',userprofile.as_view(), name='userprofile'),

]
