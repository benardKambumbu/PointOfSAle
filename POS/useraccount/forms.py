from importlib import import_module
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from .models import BkUser
from django import forms
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
	last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = User
		fields = ('first_name','last_name','username','password1','password2')
		widgets = { 

		'first_name': forms.TextInput (attrs={'class':'form-control'}),
		'last_name': forms.TextInput(attrs={'class':'form-control'}),
		'username': forms.TextInput(attrs={'class':'form-control'}),
		'password1': forms.TextInput(attrs={'class':'form-control'}),
		'password2': forms.TextInput(attrs={'class':'form-control'}),
		
		
		}

	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'

class BkUserForm(forms.ModelForm):
	class Meta:
		model = BkUser
		fields = ('profile_image','address','phoneNo','whatsapp')
		widgets = {


		'phoneNo': forms.TextInput(attrs={'class':'form-control'}),
		'address': forms.TextInput(attrs={'class':'form-control'}),
		'whatsapp': forms.TextInput(attrs={'class':'form-control'}),
		'position': forms.TextInput(attrs={'class':'form-control'}),
		'profile_image': forms.FileInput(attrs={'class':'form-control'}),
		
		}


#class LoginForm(AunthenticationForm):
#	username =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#	password =forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
#	email =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))