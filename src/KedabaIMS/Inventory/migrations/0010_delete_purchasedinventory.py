# Generated by Django 3.2.19 on 2023-05-07 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0009_purchasedinventory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PurchasedInventory',
        ),
    ]