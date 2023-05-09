from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.

class ItemCategoryAdmin(ImportExportModelAdmin):
    pass
    fields = ['name', 'description']
    list_display = ['name', 'description']
    search_fields = ['name', 'description']
    list_filter = ['name']
    list_display_links = ['name', 'description']
    # readonly_fields = ('id')
    list_per_page = 10
    list_select_related = True


    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    class Meta:
        model = ItemCategory

admin.site.register(ItemCategory, ItemCategoryAdmin)


class ItemTypeAdmin(ImportExportModelAdmin):
    pass
    fields = ['Item_category', 'name', 'description']
    list_display = ['Item_category', 'name', 'description']
    search_fields = ['Item_category', 'name', 'description']
    list_filter = ['Item_category']
    list_display_links = ['Item_category', 'name', 'description']
    # readonly_fields = ('id')
    list_per_page = 10
    list_select_related = True

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    class Meta:
        model = ItemType

admin.site.register(ItemType, ItemTypeAdmin)

class ItemPriceAdmin(ImportExportModelAdmin):
    pass
    fields = [('Item_category', 'Item_type'), ('Sale_single_price')]
    list_display = ['Item_category', 'Item_type', 'Sale_single_price']
    search_fields = ['Item_category', 'Item_type', 'Sale_single_price']
    list_filter = ['Item_category','Item_type', 'Created_date']
    list_display_links = ['Item_category', 'Item_type', 'Sale_single_price']
    readonly_fields = ('Created_date', 'Created_by', 'Modified_date', 'Modified_by',)
    list_per_page = 10
    list_select_related = True


    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    class Meta:
        model = ItemPrice

admin.site.register(ItemPrice, ItemPriceAdmin)


class ImporterAdmin(ImportExportModelAdmin):
    pass
    fields = [('name', 'sales_person'), ('phone_number', 'license')]
    list_display = ['id', 'name', 'phone_number', 'sales_person', 'license']
    search_fields = ['id', 'name', 'phonenumber', 'sales_person', 'license']
    list_filter = ['name']
    list_display_links = ['id', 'name', 'phone_number', 'sales_person', 'license']
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by',)
    list_per_page = 10
    list_select_related = True

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    class Meta:
        model = Importer

admin.site.register(Importer, ImporterAdmin)

class CustomerAdmin(ImportExportModelAdmin):
    pass
    fields = [('pharmacy_name','owner_name'), ('license_number','license'), ('phone_number', 'address')]
    list_display = ['id', 'pharmacy_name','owner_name', 'license_number','license', 'phone_number', 'address']
    search_fields = ['id', 'pharmacy_name','owner_name', 'license_number','license', 'phone_number', 'address']
    list_filter = ['license_number']
    list_display_links = ['id', 'pharmacy_name','owner_name', 'license_number','license', 'phone_number', 'address']
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by',)
    list_per_page = 10
    list_select_related = True
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    class Meta:
        model = Customer

admin.site.register(Customer, CustomerAdmin)

class MeasurementAdmin(ImportExportModelAdmin):
    pass
    fields = ['name', 'description']
    list_display = ['name', 'description']
    search_fields = ['name', 'description']
    list_filter = ['name']
    list_display_links = ['name', 'description']
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by',)
    list_per_page = 10
    list_select_related = True

    class Meta:
        model = Measurement

admin.site.register(Measurement, MeasurementAdmin)