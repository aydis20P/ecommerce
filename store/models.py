from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=16)
	email = models.CharField(max_length=45)
	password = models.CharField(max_length=16)
	isPrimary = models.BooleanField()
	familyCode = models.CharField(max_length=45)

	def __str__(self):
		return self.name


class Item(models.Model):
	name = models.CharField(max_length=45)
	description = models.CharField(max_length=45)
	price = models.FloatField()
	image = models.CharField(max_length=45)

	def __str__(self):
		return self.name

class Order(models.Model):
	dateTime = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.id)

class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=0)
	dateTimeOI = models.DateTimeField(auto_now_add=True)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)


	def __str__(self):
		return str(self.order + self.item)

class UserOrder(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	order = models.ForeignKey(Order, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.customer + self.order)