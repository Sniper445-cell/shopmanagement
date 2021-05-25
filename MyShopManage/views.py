from django.shortcuts import render
from .models import *

def ownerPage(request):
	shoplists = ShopList.objects.all()
	context = {'shoplists':shoplists}
	return render(request, 'myshopmanage/shoplist.html', context)

def managePage(request):
	shopmanagers = ShopManager.objects.all()
	context = { 'shopmanagers':shopmanagers}
	return render(request, 'myshopmanage/shopmanager.html', context) 

def employePage(request):
	shopemployees = Shopemployee.objects.all()
	context = {'shopemployees':shopemployees}
	return render(request, 'myshopmanage/shopemployee.html', context)