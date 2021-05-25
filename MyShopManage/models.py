from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ShopList(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200, null = True)
	image = models.ImageField(null=True, blank=True)
	#manager = models.CharField(max_length=200)
	#employee = models.ForeignKey(ShopEmployee, null = True, on_delete = models.SET_NULL)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ' '
		return url
	

class ShopManager(models.Model):
	shop = models.ManyToManyField(ShopList)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)
	#level = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ' '
		return url


class Shopemployee(models.Model):
	shop = models.ManyToManyField(ShopList)
	manager = models.ManyToManyField(ShopManager)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ' '
		return url