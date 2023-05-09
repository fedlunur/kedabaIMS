from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.shortcuts import redirect
from django.db import connection
from django.conf.urls import url
from django.http import HttpResponse
# import csv
from django.utils import timezone
import datetime
from datetime import datetime
from .models import *
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
# Register your models here.
class DailySaleReportAdmin(admin.ModelAdmin):
    fields = ['id','sale_total_price', 'sales_date']
    list_display = ['id','sale_total_price', 'sales_date']
    search_fields = ['id','sale_total_price', 'sales_date']
    list_filter = ['sales_date']
    readonly_fields=('id','sale_total_price', 'sales_date',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    class Meta:
        model = DailySaleReport

admin.site.register(DailySaleReport, DailySaleReportAdmin)


class AvailableForSaleAdmin(admin.ModelAdmin):
    fields = ['id','Item_category_id', 'Item_type_id', 'Quantity']
    list_display = ['id','Item_category_id', 'Item_type_id', 'Quantity']
    search_fields = ['id','Item_category_id', 'Item_type_id', 'Quantity']
    list_filter = ['Item_category_id']
    readonly_fields=('id','Item_category_id', 'Item_type_id', 'Quantity',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    class Meta:
        model = AvailableForSale

admin.site.register(AvailableForSale, AvailableForSaleAdmin)

class EndingInventoryAdmin(admin.ModelAdmin):
    fields = ['id','Item_category_id', 'Item_type_id', 'Ending_inventory']
    list_display = ['id','Item_category_id', 'Item_type_id', 'Ending_inventory']
    search_fields = ['id','Item_category_id', 'Item_type_id', 'Ending_inventory']
    list_filter = ['Item_category_id']
    readonly_fields=('id','Item_category_id', 'Item_type_id', 'Ending_inventory',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    class Meta:
        model = EndingInventory

admin.site.register(EndingInventory, EndingInventoryAdmin)

class InventoryBalanceAdmin(admin.ModelAdmin):
    fields = ['id','Item_category_id', 'Item_type_id', 'begin_items', 'purchased_items', 'Sold_items', 'Available_for_sale', 'Ending_inventory']
    list_display = ['id','Item_category_id', 'Item_type_id', 'begin_items', 'purchased_items', 'Sold_items', 'Available_for_sale', 'Ending_inventory']
    search_fields = ['id','Item_category_id', 'Item_type_id', 'begin_items', 'purchased_items', 'Sold_items', 'Available_for_sale', 'Ending_inventory']
    list_filter = ['Item_category_id']
    readonly_fields=('id','Item_category_id', 'Item_type_id', 'begin_items', 'purchased_items', 'Sold_items', 'Available_for_sale', 'Ending_inventory')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    class Meta:
        model = InventoryBalance

admin.site.register(InventoryBalance, InventoryBalanceAdmin)


class ImporterReportAdmin(admin.ModelAdmin):
    fields = ['id','name', 'Item_category_id', 'Item_type_id', 'batch', 'Total_birr', 'discount', 'Modified_date']
    list_display = ['id', 'name', 'Item_category_id', 'Item_type_id', 'batch', 'Total_birr', 'discount', 'Modified_date']
    search_fields = ['id', 'name', 'Item_category_id', 'Item_type_id', 'batch', 'Total_birr', 'discount', 'Modified_date']
    list_filter = ['Item_category_id']
    readonly_fields=('id', 'name', 'Item_category_id', 'Item_type_id', 'batch', 'Total_birr', 'discount', 'Modified_date')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    class Meta:
        model = ImporterReport

admin.site.register(ImporterReport, ImporterReportAdmin)