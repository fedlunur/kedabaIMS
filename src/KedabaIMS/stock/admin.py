# from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
# from .models import *

# # Register your models here.
# class BeginInventoryAdmin(ImportExportModelAdmin):
#     pass
#     fields = [('name','batch'), ('quantity', 'unit_purchased_price'), ('expired_date'), ('category', 'importer'), ('date_of_purchased','discount'), ('min_level', 'max_level'), ('created_at', 'created_by', 'updated_at', 'updated_by')]
#     list_display = ['id', 'name','batch', 'quantity', 'unit_purchased_price', 'expired_date', 'category', 'importer', 'date_of_purchased', 'min_level', 'max_level']
#     search_fields = ['id', 'name','batch', 'quantity', 'unit_purchased_price', 'expired_date', 'category', 'importer', 'date_of_purchased', 'min_level', 'max_level']
#     list_filter = ['category', 'importer']
#     list_display_links = ['id', 'name','batch', 'quantity', 'unit_purchased_price', 'expired_date', 'category', 'importer', 'date_of_purchased', 'min_level', 'max_level']
#     readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by',)
#     list_per_page = 10
#     list_select_related = True

#     def get_actions(self, request):
#         actions = super().get_actions(request)
#         if 'delete_selected' in actions:
#             del actions['delete_selected']
#         return actions

#     class Meta:
#         model = BeginInventory

# admin.site.register(BeginInventory, BeginInventoryAdmin)


# class PurchaedInventoryAdmin(ImportExportModelAdmin):
#     pass
#     fields = [('name','batch'), ('quantity', 'unit_purchased_price'), ('expired_date'), ('catagory', 'importer'), ('date_of_purchased', 'discount'), ('min_level', 'max_level'), ('created_at', 'created_by', 'updated_at', 'updated_by')]
#     list_display = ['id', 'name','batch', 'quantity', 'unit_purchased_price', 'expired_date', 'catagory', 'importer', 'date_of_purchased', 'min_level', 'max_level']
#     search_fields = ['id', 'name','batch', 'quantity', 'unit_purchased_price', 'expired_date', 'catagory', 'importer', 'date_of_purchased', 'min_level', 'max_level']
#     list_filter = ['catagory', 'importer']
#     list_display_links = ['id', 'name','batch', 'quantity', 'unit_purchased_price', 'expired_date', 'catagory', 'importer', 'date_of_purchased', 'min_level', 'max_level']
#     readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by',)
#     list_per_page = 10
#     list_select_related = True

#     def get_actions(self, request):
#         actions = super().get_actions(request)
#         if 'delete_selected' in actions:
#             del actions['delete_selected']
#         return actions

#     class Meta:
#         model = PurchaedInventory

# admin.site.register(PurchaedInventory, PurchaedInventoryAdmin)