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

class NewSaleInline(admin.TabularInline):
    model = NewSale
    extra = 0
    readonly_fields = ('Sale_single_price', 'Sale_total_price',)

class SaleAdmin(ImportExportModelAdmin):
    pass
    inlines = [NewSaleInline]
    fields = [('sales_date', 'employee', 'customer'), ('total')]
    list_display = ['id', 'sales_date','employee', 'customer', 'total']
    search_fields = ['id', 'sales_date','employee', 'customer', 'total']
    list_filter = ['sales_date']
    list_display_links = ['id', 'id', 'sales_date','employee', 'customer', 'total']
    readonly_fields = ('total', 'created_at', 'created_by', 'updated_at', 'updated_by',)
    list_per_page = 10
    list_select_related = True

    def response_add(self, request, new_object):
        obj = self.after_saving_model_and_related_inlines(new_object)
        return super(SaleAdmin, self).response_add(request, obj)

    def response_change(self, request, obj):
        obj = self.after_saving_model_and_related_inlines(obj)
        return super(SaleAdmin, self).response_change(request, obj)

    def after_saving_model_and_related_inlines(self, obj):

        invoice_lines = NewSale.objects.filter(Sale_total_price=obj.pk)

        obj.total = 0
        for line in invoice_lines:
            obj.total=obj.total+line.Sale_total_price
        obj.save()
        return obj

    def save_model(self, request, obj, form, change):
    	if change:
    		obj.updated_at = request.user
    		obj.updated_at = datetime.now()
    	obj.save()

    class Meta:
        model = Sale

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Sale, SaleAdmin)