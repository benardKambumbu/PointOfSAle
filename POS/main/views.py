from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from django.urls import reverse_lazy
from .models import Shop, Product
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
import random
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import string
from django.views.generic import ListView, DetailView,DeleteView,CreateView, UpdateView
from useraccount.models import *
from .forms import *

def bkuserView(request, context):
    if request.user.is_anonymous == False:
        
        context['user'] = request.user
        if BkUser.objects.filter(bkuser = request.user):
            context['bkuser']= BkUser.objects.get(bkuser= request.user)
		

def dashboard(request):
	context={}
	if request.user.is_anonymous == False: 
		context['user'] = request.user
		if BkUser.objects.filter(bkuser = request.user):
			context['bkuser']= BkUser.objects.get(bkuser= request.user)
			
	else:
		return redirect('login') 
	return render(request, 'indexdash.html',context)

def coming(request):
    context={}  
    return render(request, 'coming_soon.html',context)
   

# class Calender(DetailView):
# 	model = Shop
# 	template_name = 'calendar.html'
def createProduct(request):
	context={}
	if request.user.is_anonymous == False: 
		context['user'] = request.user
		if BkUser.objects.filter(bkuser = request.user):
			context['bkuser']= BkUser.objects.get(bkuser= request.user)
			
	else:
		return redirect('login') 
	return render(request,'calendar.html',context)




def addProduct(request):
	print('save1')
	if request.POST:
		if request.user.is_anonymous == True:
			return redirect('login')
		print('save1')
		if Product.objects.filter(product_part_number = request.POST['productName']).exists() or Product.objects.filter(product_part_number = request.POST['productNo']).exists():
			return redirect('dash-calender')
		else:
			
			shop = request.POST['shopName']
			if shop == 1 or shop == '1':
				shop1 = Shop.objects.get(id = 1)
			elif shop == 2 or shop == '2':
				shop1 = Shop.objects.get(id = 2)
			
			product_name = request.POST['productName']
			product_description = request.POST['productDescription']
			product_model = request.POST['productModel']
			product_part_number = request.POST['productNo']
			product_price = request.POST['productPrice']
			product_promote = request.POST['productPromote']
			if product_promote == True:
				product_promotion = request.POST['productPromotion']
				product_promote = True
			else:
				product_promotion = ''
				product_promote = False
			product_size = request.POST['productSize']
			product_quantity= request.POST['quantity']
			product_specifications = request.POST['productSpecification']
			product_last_price = request.POST['lastPrice']
			print(product_promotion)
			x  =Product.objects.create(user = request.user,shop_name=shop1, product_name=product_name,product_description=product_description,
			product_model=product_model,product_part_number=product_part_number,product_price=product_price,product_promote=product_promote,
			product_promotion=product_promotion,product_size=product_size,product_quantity=product_quantity,product_specifications=product_specifications,
			product_last_price=product_last_price)
			x.save()
			return redirect('dash-calender')
			
			
	return redirect('index')

def addCart(request,pk):
	id = pk
	if Product.objects.filter(id = id).exists():
		if request.user.is_anonymous == True:
			return redirect('login')
		x = Product.objects.get(id = id)
		print(x)
		if Cart.objects.filter(product_part_number = x.product_part_number).exists() or Cart.objects.filter(product_part_number = x.product_part_number).exists():
			print('xxxxxxxxxxxx')
			return redirect('dash-shopcart')
			
		else:
			print('Yyyy')
			shop1 = x.shop_name
			product_name = x.product_name
			product_description = x.product_description
			product_model = x.product_model
			product_part_number = x.product_part_number
			product_price = x.product_price
			product_promote = x.product_promote
			if product_promote == True:
				product_promotion = x.product_promotion
				x.product_promote = True
			else:
				product_promotion = ''
				x.product_promote = False
			product_size = x.product_size
			product_quantity= 1
			product_specifications = x.product_specifications
			product_last_price = x.product_last_price
			code = ''
			
			if 'code' in request.session:
				code = request.session['code']
			else:
				code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
				request.session['code']	= code
			customer = code		
			x =Cart.objects.create(user = request.user,customer = customer,shop_name=shop1, product_name=product_name,product_description=product_description,
			product_model=product_model,product_part_number=product_part_number,product_price=product_price,product_promote=product_promote,
			product_promotion=product_promotion,product_size=product_size,product_quantity=product_quantity,product_specifications=product_specifications,
			product_last_price=product_last_price)
			
			x.save()
			return redirect('dash-shopcart')
			
			
	return redirect('dash-shopcart')

class deleteCart(DeleteView):
	model = Cart
	template_name= 'deleteCart.html'
	success_url= reverse_lazy('dash-shopcart')
	


def inventory_view(request):
	context={}
	if request.user.is_anonymous == False: 
		context['user'] = request.user
		if BkUser.objects.filter(bkuser = request.user):
			context['bkuser']= BkUser.objects.get(bkuser= request.user)
			
	else:
		return redirect('login') 
	products = Product.objects.all()
	context['products'] = products
	if 'code' in request.session:
		context['cartlist'] = Cart.objects.filter(customer = request.session['code'])
	else:
		context['cartlist']= None
	return render(request,'inventory.html',context)

def inventory_view1(request):
	context={}
	if request.user.is_anonymous == False: 
		context['user'] = request.user
		if BkUser.objects.filter(bkuser = request.user):
			context['bkuser']= BkUser.objects.get(bkuser= request.user)
			
	else:
		return redirect('login')
	x1 = Shop.objects.filter(id = 1) 
	products = Product.objects.filter(shop_name = x1)
	context['products'] = products
	if 'code' in request.session:
		context['cartlist'] = Cart.objects.filter(customer = request.session['code'])
	else:
		context['cartlist']= None
	return render(request,'inventory.html',context)

def inventory_view2(request):
	
	context={}
	if request.user.is_anonymous == False: 
		context['user'] = request.user
		if BkUser.objects.filter(bkuser = request.user):
			context['bkuser']= BkUser.objects.get(bkuser= request.user)
			
	else:
		return redirect('login') 
	x2 = Shop.objects.filter(id = 2) 
	products = Product.objects.filter(shop_name = x2.id)
	context['products'] = products
	if 'code' in request.session:
		context['cartlist'] = Cart.objects.filter(customer = request.session['code'])
	else:
		context['cartlist']= None
	return render(request,'inventory.html',context)

def pos_view(request):
	context={}
	if request.user.is_anonymous == False: 
		context['user'] = request.user
		if BkUser.objects.filter(bkuser = request.user):
			context['bkuser']= BkUser.objects.get(bkuser= request.user)
			
	else:
		return redirect('login') 
	products = Product.objects.all()
	context['products'] = products
	if 'code' in request.session:
		context['cartlist'] = Cart.objects.filter(customer = request.session['code'])
		x = Cart.objects.filter(customer = request.session['code'])
	else:
		context['cartlist']= None
		x = ''
	
	context['cartTotal'] = len(x)
	ct = 0
	
	if context['cartlist'] != None:
		for xy in x:
			ct += int(xy.product_price)

	context['total'] = ct

	return render(request,'shopping-cart.html',context)

def cancelCart(request):
	if 'code' in request.session:
		
		x = Cart.objects.filter(customer = request.session['code'])
		for xy in x:
			xy.delete()
		del request.session['code']
	return redirect('dash-shopcart')

def checkout_view(request):
	if request.POST:
		
		customer = ''
		if 'customer' in request.POST:
			customer = request.POST['customer']
		
		
		shop1 = Shop.objects.get(id=1)
		if 'code' in request.session:
			x = Cart.objects.filter(customer = request.session['code'])
			code = request.session['code']
			list = ''
			totals12 = 0
			for x1 in x:
				buyingPrice = ''
				list = list + ', ' + x1.product_name
				if 'buyingPrice' in request.POST:
					buyingPrice = request.POST['buyingPrice' + str(x1.id) ]
				total12 = int(request.POST['quantity'+ str(x1.id)] ) * int(x1.product_price)
				totals12 = totals12 + total12
				commit =CheckedOut.objects.create(user = request.user,code=code,customer = customer,shop_name=shop1, product_name=x1.product_name,product_description=x1.product_description,
						product_model=x1.product_model,product_part_number=x1.product_part_number,product_price=x1.product_price,product_promote=x1.product_promote,
						product_promotion=x1.product_promotion,product_size=x1.product_size,product_specifications=x1.product_specifications,
						product_last_price=x1.product_last_price, product_buying_price=buyingPrice, product_quantity = request.POST['quantity'+ str(x1.id)], total= total12)
			if commit:
				commit.save()
			trans = Transactions.objects.create(user = request.user,code = code,customer=customer, shop_name = shop1,
			products = list,paymentMethod = 'usd',total=totals12)
			trans.save()

			x1.delete()

			
			return cancelCart(request)

			


class Productdetail(UpdateView):

	def get_context_data(self, **kwargs):

		context = super().get_context_data(**kwargs)
		if self.request.user.is_anonymous == False:
			if Product.objects.filter(user = self.request.user):
				context['owner'] = True
		# return JsonResponse(letters)
		return context

	def form_valid(self, form):
		self.object = form.save(commit=False)
		if self.request.user.is_anonymous == True:
			return redirect('login')
		else:
			self.object.user = self.request.user
			self.object.save()
			
			return redirect('index')

	
class Checkout(DetailView):
	model = Product
	template_name = 'apps-ecommerce-checkout.html'

class Orderdetail(DetailView):
	model = Product
	template_name = 'apps-ecommerce-orders-details.html'

class Orders(DetailView):
	model = Product
	template_name = 'inventory.html'        

def Products(request,pk):
	context={}
	if request.user.is_anonymous == False: 
		context['user'] = request.user
		if BkUser.objects.filter(bkuser = request.user):
			context['bkuser']= BkUser.objects.get(bkuser= request.user)
			
	else:
		return redirect('login') 
	products = CheckedOut.objects.all()
	context['products'] = products
	if 'code' in request.session:
		context['cartlist'] = Cart.objects.filter(customer = request.session['code'])
	else:
		context['cartlist']= None
	return render(request,'history.html',context)


def Products1(request,pk):
	context={}
	if request.user.is_anonymous == False: 
		context['user'] = request.user
		if BkUser.objects.filter(bkuser = request.user):
			context['bkuser']= BkUser.objects.get(bkuser= request.user)
			
	else:
		return redirect('login') 
	products = Transactions.objects.all()
	context['products'] = products
	if 'code' in request.session:
		context['cartlist'] = Cart.objects.filter(customer = request.session['code'])
	else:
		context['cartlist']= None
	return render(request,'history1.html',context)


def Products2(request,pk):
	context={}
	if request.user.is_anonymous == False: 
		context['user'] = request.user
		if BkUser.objects.filter(bkuser = request.user):
			context['bkuser']= BkUser.objects.get(bkuser= request.user)
			
	else:
		return redirect('login') 
	products = CheckedOut.objects.all()
	context['products'] = products
	if 'code' in request.session:
		context['cartlist'] = Cart.objects.filter(customer = request.session['code'])
	else:
		context['cartlist']= None
	return render(request,'history2.html',context)

class Productdetail(DetailView):
	model = Product
	template_name = 'history2.html'	




class Gmap(DetailView):
	model = Product
	template_name = 'maps-google.html'  

class Faq(DetailView):
	model = Product
	template_name = 'pages-faq.html'  
    
class Profile(DetailView):
	model = Product
	template_name = 'pages-profile.html'  

class Maintenance(DetailView):
	model = Product
	template_name = 'pages-maintenance.html'     

class P404(DetailView):
	model = Product
	template_name = 'pages-500.html'   

class P500(DetailView):
	model = Product
	template_name = 'pages-500.html'   
   

