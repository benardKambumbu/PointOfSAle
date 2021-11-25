from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import BkUserForm, RegisterUserForm
from .models import BkUser, verify_email
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random
import string
from main.models import *
# Create your views here.
class UserRegister(generic.CreateView):
    form_class =  RegisterUserForm
    model = User
    template_name = 'registration/register.html'
    success_url = reverse_lazy('register2')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'verificationError' in self.request.session:
            del self.request.session['verificationError']
        if 'emailerror' in self.request.session:
            context['error'] = self.request.session['emailerror']
                
        return context


    def form_valid(self, form):
        self.object = form.save(commit=False)
        code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        
        self.request.session['username'] = self.object.username
        self.object.save()
        #user = User.objects.get(username = self.object.username, email = self.object.email)
        #verification = verify_email.objects.create( user = user, email = self.object.email, verification_code = code) 
        #verification.save()
        return redirect('register2')

class UserRegister2(generic.CreateView):
    model = BkUser
    form_class = BkUserForm
    template_name = 'registration/register1.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if 'verificationError' in self.request.session:
            context['error'] = 'user exists'
    
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        position = self.request.POST['position']
        shop = self.request.POST['shop']
        print(11111111111)
       
        print(2222222222222222)
        if position == '1' or position == 1:
            self.object.position = 'admin'
        elif position == '2' or position == 2:
            self.object.position = 'cashier'
        elif position == '3' or position == 3:
            self.object.position = 'accountant'
        elif position == '4' or position == 4:
            self.object.position = 'member'
        else:
            self.object.position = 'cashier'
        
        if shop == '1' or shop == 1:
            self.object.shop = Shop.objects.get(id = 1)
        elif shop == '2' or shop == 2:
            self.object.shop = Shop.objects.get(id = 2)
        else:
            self.object.shop = Shop.objects.get(id = 1)

        self.object.bkuser = User.objects.get(username = self.request.session['username'])
        self.object.save()
        self.request.session['verificationSuccess'] = True
        return redirect('login')
  

class UserRegister22(generic.CreateView):
    model = BkUser
    form_class = BkUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('bkaccounts')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.bkuser = self.request.user
        self.object.save()
        return redirect('bkaccounts')

class userprofile(generic.UpdateView):
    model = BkUser
    form_class =BkUserForm
    template_name= 'registration/register.html'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.bkuser = self.request.user
        self.object.save()
        return redirect('bkaccounts')

def bkaccounts(request):
    context={}

    if request.user.is_anonymous == False:
        
        context['user'] = request.user
        if BkUser.objects.filter(bkuser = request.user):
            context['bkuser']= BkUser.objects.get(bkuser= request.user)
    
    return render(request, 'indexdash.html',context)

def mail(request):
    try:
        send_mail(
        'bkafricaZim',
        'bkafricaZim online platform\n\n\n' + request.session['code'],
        'blackmankriativity@gmail.com',
        [request.session['email']],
        fail_silently=False,)
    except:
        request.session['email1'] = 'Could not send an email to the provided email, check your network status or change the provided emqail' + request.session['email']
        return redirect('register')

    return redirect('verification')

# def verify(request):
    
#     if 'email' in request.session:
#         x = request.session['email']
#     else:
#         x = ''
#     context = {'email': x}
#     if Transition1.objects.filter(email = x).exists():
#         profile = Transition1.objects.get(email = x)
#         context['profile'] = profile
    
#     return render(request,'verification.html', context)

