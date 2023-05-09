# Generated by Django 3.2.19 on 2023-05-09 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_availableforsale'),
    ]

    operations = [
        migrations.CreateModel(
            name='EndingInventory',
            fields=[
                ('id', models.CharField(max_length=150, primary_key=True, serialize=False, unique=True)),
                ('Item_category_id', models.CharField(max_length=250)),
                ('Item_type_id', models.CharField(max_length=100)),
                ('Ending_inventory', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'Endinginventory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InventoryBalance',
            fields=[
                ('id', models.CharField(max_length=150, primary_key=True, serialize=False, unique=True)),
                ('Item_category_id', models.CharField(max_length=250)),
                ('Item_type_id', models.CharField(max_length=100)),
                ('begin_items', models.CharField(max_length=150)),
                ('purchased_items', models.CharField(max_length=150)),
                ('Sold_items', models.CharField(max_length=150)),
                ('Available_for_sale', models.CharField(max_length=150)),
                ('Ending_inventory', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'Inventorybalance',
                'managed': False,
            },
        ),
    ]
