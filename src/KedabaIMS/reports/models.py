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

class DailySaleReport(models.Model):
	id = models.CharField(primary_key = True, max_length = 150, unique = True)
	# GeneralCashReport = models.ForeignKey(GeneralCashReport, on_delete=models.CASCADE)
	sale_total_price = models.CharField(max_length=250)
	sales_date = models.DateField()

	def __str__(self):
		return "%s" % self.id

	class Meta:
		managed = False
		db_table = "gsale"


class AvailableForSale(models.Model):
	id = models.CharField(primary_key = True, max_length = 150, unique = True)
	# GeneralCashReport = models.ForeignKey(GeneralCashReport, on_delete=models.CASCADE)
	Item_category_id = models.CharField(max_length=250)
	Item_type_id = models.CharField(max_length=100)
	Quantity = models.CharField(max_length=150)

	def __str__(self):
		return "%s" % self.id

	class Meta:
		managed = False
		db_table = "Inventoryunion"

class EndingInventory(models.Model):
	id = models.CharField(primary_key = True, max_length = 150, unique = True)
	# GeneralCashReport = models.ForeignKey(GeneralCashReport, on_delete=models.CASCADE)
	Item_category_id = models.CharField(max_length=250)
	Item_type_id = models.CharField(max_length=100)
	Ending_inventory = models.CharField(max_length=150)

	def __str__(self):
		return "%s" % self.id

	class Meta:
		managed = False
		db_table = "Ending_inventory"


class InventoryBalance(models.Model):
	id = models.CharField(primary_key = True, max_length = 150, unique = True)
	# GeneralCashReport = models.ForeignKey(GeneralCashReport, on_delete=models.CASCADE)
	Item_category_id = models.CharField(max_length=250)
	Item_type_id = models.CharField(max_length=100)
	begin_items = models.CharField(max_length=150)
	purchased_items = models.CharField(max_length=150)
	Sold_items = models.CharField(max_length=150)
	Available_for_sale = models.CharField(max_length=150)
	Ending_inventory = models.CharField(max_length=150)

	def __str__(self):
		return "%s" % self.id

	class Meta:
		managed = False
		db_table = "Inventorybalance"

class ImporterReport(models.Model):
	id = models.CharField(primary_key = True, max_length = 150, unique = True)
	name = models.CharField(max_length=250)
	Item_category_id = models.CharField(max_length=250)
	Item_type_id = models.CharField(max_length=100)
	batch = models.CharField(max_length=100)
	Total_birr = models.CharField(max_length=150)
	discount = models.CharField(max_length=150)
	Modified_date = models.CharField(max_length=150)

	def __str__(self):
		return "%s" % self.id

	class Meta:
		managed = False
		db_table = "Purchased_items_by_importer"