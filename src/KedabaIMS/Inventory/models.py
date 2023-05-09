from django.db import models
# import os
from import_export import resources
from django.db.models import Subquery, OuterRef
from django.db import connection
from django.utils import timezone
import datetime
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
from django_currentuser.db.models import CurrentUserField
from django.urls import reverse
from django.http import HttpResponse
from setup.models import *
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.
class BeginInventory(models.Model):
	id = models.AutoField(primary_key=True, unique=True)
	Item_category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
	Item_type = ChainedForeignKey(ItemType, chained_field="Item_category", chained_model_field="Item_category", show_all=False, auto_choose=True, sort=True)
	Unit = models.ForeignKey(Measurement, on_delete=models.CASCADE)
	Quantity = models.PositiveIntegerField()
	min_level=models.PositiveIntegerField(default=5)
	unit_purchased_price = models.DecimalField(max_digits = 5, decimal_places = 2)
	purchased_total_price = models.DecimalField(max_digits = 11, decimal_places = 2, null=True, blank=True)
	importer=models.ForeignKey(Importer,on_delete=models.CASCADE)
	batch=models.CharField(max_length=200)   
	expired_date=models.DateField() 
	discount=models.FloatField()

	Remark = models.CharField(max_length=250, null=True, blank=True)
	
	Created_date = models.DateField(auto_now=True)
	Created_by = CurrentUserField()
	Modified_date = models.DateTimeField(auto_now=True)
	Modified_by = CurrentUserField(related_name="m7")

	def __str__(self):
		return "%s" % self.Item_type

	class Meta:
		verbose_name_plural = "Begin inventories"

	def save(self, *args, **kwargs):
		self.purchased_total_price = self.Quantity * self.unit_purchased_price
		super(BeginInventory, self).save(*args, **kwargs)

class PurchasedInventory(models.Model):
	id = models.AutoField(primary_key=True, unique=True)
	Item_category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
	Item_type = ChainedForeignKey(ItemType, chained_field="Item_category", chained_model_field="Item_category", show_all=False, auto_choose=True, sort=True)
	Unit = models.ForeignKey(Measurement, on_delete=models.CASCADE)
	Quantity = models.PositiveIntegerField()
	min_level=models.PositiveIntegerField(default=5)
	unit_purchased_price = models.DecimalField(max_digits = 5, decimal_places = 2)
	purchased_total_price = models.DecimalField(max_digits = 11, decimal_places = 2, null=True, blank=True)
	importer=models.ForeignKey(Importer,on_delete=models.CASCADE)
	batch=models.CharField(max_length=200)   
	expired_date=models.DateField() 
	discount=models.FloatField()

	Remark = models.CharField(max_length=250, null=True, blank=True)
	
	Created_date = models.DateField(auto_now=True)
	Created_by = CurrentUserField()
	Modified_date = models.DateTimeField(auto_now=True)
	Modified_by = CurrentUserField(related_name="m27")

	def __str__(self):
		return "%s" % self.Item_type

	class Meta:
		verbose_name_plural = "Purchased inventories"

	def save(self, *args, **kwargs):
		self.purchased_total_price = self.Quantity * self.unit_purchased_price
		super(PurchasedInventory, self).save(*args, **kwargs)