from django.db import models
from django.utils import timezone
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
# from inventory.models import *
from smart_selects.db_fields import ChainedForeignKey
# from django.db.models.query import QuerySet
# import numpy as np

# Create your models here.
class Sale(models.Model):
	id = models.AutoField(primary_key=True, unique=True)
	sales_date=models.DateField(default=timezone.now)
	employee=models.ForeignKey(User,on_delete=models.CASCADE)
	customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
	total = models.DecimalField(max_digits = 11, decimal_places = 2, null=True, blank=True)
	
	created_at = models.DateTimeField(auto_now_add=True)
	created_by = CurrentUserField(related_name="m16")
	updated_at = models.DateTimeField(auto_now=True)
	updated_by = CurrentUserField(related_name="m17")


	def save(self, *args, **kwargs):
         invoice_lines = NewSale.objects.filter(sale=self.id)
         self.total = 0
         for line in invoice_lines:
             self.total+=line.Sale_total_price
         super(Sale, self).save(*args, **kwargs)
	

	def __str__(self):
		return "%s" % self.customer
		
class NewSale(models.Model):
	sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
	Item_category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
	Item_type = ChainedForeignKey(ItemType, chained_field="Item_category", chained_model_field="Item_category", show_all=False, auto_choose=True, sort=True)
	quantity = models.DecimalField(max_digits = 11, decimal_places = 2)
	Sale_single_price = models.DecimalField(max_digits = 11, decimal_places = 2)
	Sale_total_price = models.DecimalField(max_digits = 11, decimal_places = 2, null=True, blank=True)
	# Total = models.PositiveIntegerField(null=True, blank=True)
	
	def save(self, *args, **kwargs):

		p = ItemPrice.objects.get(Item_type=self.Item_type_id)
		ssp = p.Sale_single_price
		self.Sale_single_price = ssp

		self.Sale_total_price = self.quantity * ssp
		super(NewSale, self).save(*args, **kwargs)


# class Sale(models.Model):
#         id = models.AutoField(primary_key=True, unique=True)
#         sales_date=models.DateField(default=timezone.now)
#         customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
#         product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
#         product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

#         created_at = models.DateTimeField(auto_now_add=True)
#         created_by = CurrentUserField()
#         updated_at = models.DateTimeField(auto_now=True)
#         updated_by = CurrentUserField(related_name="m4")

#         def __str__(self):
#                 #  return self.customer + '  '+self.employee.first_name ++self.salesDate 
#                 return self.customer.name
			
