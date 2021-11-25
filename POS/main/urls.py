from django.urls import path
from .views import *
from django.contrib import admin
from django.urls import include, re_path
from .views import *
from django.conf.urls import url




urlpatterns = [
    
    path('dashboard/', dashboard, name='index'),
    path('coming_soon/', coming, name='coming-soon'),
    path('product_create/', createProduct, name='dash-calender'),
	path('addProduct/', addProduct, name='addProduct'),
	url(r'^addCart/(?P<pk>[0-9]+)/$', addCart, name='addCart'),
	path('Inventory/', inventory_view, name='inventory'),
	path('InventoryAll/', inventory_view, name='inventory1'),
	path('Inventory_shop1/', inventory_view1, name='inventory2'),
	path('Inventory_shop2/', inventory_view2, name='inventory3'),
	path('Point_of_sale/', pos_view, name='dash-shopcart'),
	url(r'^delete_cart/(?P<pk>[0-9]+)/$', deleteCart.as_view(), name='deleteCart'),
	path('cancel_cart/', cancelCart, name='cancelCart'),
	path('checkout_view/', checkout_view, name='checkout'),

	url(r'^dash_checkout/(?P<pk>[0-9]+)/$', Checkout.as_view(), name='dash-checkout'),
	url(r'^dash_orderdetail/(?P<pk>[0-9]+)/$', Orderdetail.as_view(), name='dash-orderdetail'),
	
	url(r'^dash_productdetail/(?P<pk>[0-9]+)/$', Productdetail.as_view(), name='dash-productdetail'),
	url(r'^dash_products/(?P<pk>[0-9]+)/$', Products, name='dash-products'),
	url(r'^dash_products_checkedout/(?P<pk>[0-9]+)/$', Products, name='dash-products1'),
	url(r'^dash_products2/(?P<pk>[0-9]+)/$', Products1, name='dash-products2'),
	url(r'^dash_products3/(?P<pk>[0-9]+)/$', Products2, name='dash-products3'),
	# url(r'^dash_shopcart/(?P<pk>[0-9]+)/$', Shoppingcart.as_view(), name='dash-shopcart'),
	url(r'^dash_gmap/(?P<pk>[0-9]+)/$', Gmap.as_view(), name='dash-gmap'),
	url(r'^dash_faq/(?P<pk>[0-9]+)/$', Faq.as_view(), name='dash-faq'),
	url(r'^dash_profile/(?P<pk>[0-9]+)/$', Profile.as_view(), name='dash-profile'),
	url(r'^oops/(?P<pk>[0-9]+)/$', Maintenance.as_view(), name='dash-maintanance'),
	# url(r'^page_not_found/(?P<pk>[0-9]+)/$', P404.as_view(), name='dash-404'),
	url(r'^error_500/(?P<pk>[0-9]+)/$', P500.as_view(), name='dash-500'),
	# url(r'^coming_soon/(?P<pk>[0-9]+)/$', coming, name='coming-soon')
	
    
    

]