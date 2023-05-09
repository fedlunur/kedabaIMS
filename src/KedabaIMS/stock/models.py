# from django.db import models
# from django_currentuser.middleware import (
#     get_current_user, get_current_authenticated_user)
# from django_currentuser.db.models import CurrentUserField
# from setup.models import * 

# Create your models here.class Importer(models.Model):
# class BeginInventory(models.Model):
#         id = models.AutoField(primary_key=True, unique=True)
#         name=models.CharField(max_length=200)
#         batch=models.CharField(max_length=200)
#         quantity=models.CharField(max_length=100) 
#         unit_purchased_price=models.CharField(max_length=100,null=True) 
#         expired_date=models.CharField(max_length=100,null=True) 
#         category=models.ForeignKey(ItemCategory,on_delete=models.CASCADE)
#         importer=models.ForeignKey(Importer,on_delete=models.CASCADE)
#         date_of_purchased=models.DateField(null=True)
#         min_level=models.IntegerField()
#         discount=models.FloatField()
#         created_at = models.DateTimeField(auto_now_add=True)
#         created_by = CurrentUserField()
#         updated_at = models.DateTimeField(auto_now=True)
#         updated_by = CurrentUserField(related_name="m1")

#         def __str__(self):
#          return self.name


# class PurchaedInventory(models.Model):
#         id = models.AutoField(primary_key=True, unique=True)
#         name=models.CharField(max_length=200)
#         batch=models.CharField(max_length=200)
#         quantity=models.CharField(max_length=100) 
#         unit_purchased_price=models.CharField(max_length=100,null=True) 
#         expired_date=models.CharField(max_length=100,null=True) 
#         catagory=models.ForeignKey(ItemCategory,on_delete=models.CASCADE)
#         importer=models.ForeignKey(Importer,on_delete=models.CASCADE)
#         date_of_purchased=models.DateField(null=True)
#         min_level=models.IntegerField()
#         max_level=models.IntegerField()
#         discount=models.FloatField()
#         created_at = models.DateTimeField(auto_now_add=True)
#         created_by = CurrentUserField()
#         updated_at = models.DateTimeField(auto_now=True)
#         updated_by = CurrentUserField(related_name="m2")
        

#         def __str__(self):
#          return self.name

