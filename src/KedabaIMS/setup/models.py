from django.db import models
import os
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
from smart_selects.db_fields import ChainedForeignKey
# Create your models here.

class ItemCategory(models.Model):
    # id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(primary_key=True, unique=True, max_length=100)
    description = models.CharField(max_length=250)
    class Meta:
        verbose_name_plural = "Item categories"

    def __str__(self):
        return "%s" % self.name

class ItemType(models.Model):
    # id = models.AutoField(primary_key=True, unique=True)
    Item_category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    name = models.CharField(primary_key=True, unique=True, max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return "%s" % self.name

class ItemPrice(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    Item_category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    Item_type = ChainedForeignKey(ItemType, chained_field="Item_category", chained_model_field="Item_category", show_all=False, auto_choose=True, sort=True)
    Sale_single_price = models.DecimalField(max_digits = 11, decimal_places = 2)
    
    Created_date = models.DateField(auto_now=True)
    Created_by = CurrentUserField()
    Modified_date = models.DateTimeField(auto_now=True)
    Modified_by = CurrentUserField(related_name="updated_byz")

    def __str__(self):
        return "%s" % self.Sale_single_price

class Measurement(models.Model):
     # id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(primary_key=True, unique=True, max_length=100)
    description = models.CharField(max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = CurrentUserField()
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = CurrentUserField(related_name="m15")

    def __str__(self):
        return "%s" % self.name   

class Importer(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name=models.CharField(max_length=200)
    sales_person=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=100) 
    license=models.FileField(max_length=200, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = CurrentUserField()
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = CurrentUserField(related_name="m10")
    
    def __str__(self):
        return self.name     

class Customer(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    pharmacy_name=models.CharField(max_length=200)
    owner_name = models.CharField(max_length=250)
    license_number = models.PositiveIntegerField(null=True, blank=True)
    license=models.FileField(max_length=200, null=True, blank=True)
    phone_number=models.CharField(max_length=100) 
    address=models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = CurrentUserField()
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = CurrentUserField(related_name="m14")
   
    def __str__(self):
    	return self.pharmacy_name   