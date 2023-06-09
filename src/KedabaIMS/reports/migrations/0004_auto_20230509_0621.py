# Generated by Django 3.2.19 on 2023-05-09 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_endinginventory_inventorybalance'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImporterReport',
            fields=[
                ('id', models.CharField(max_length=150, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('Item_category_id', models.CharField(max_length=250)),
                ('Item_type_id', models.CharField(max_length=100)),
                ('batch', models.CharField(max_length=100)),
                ('Total_birr', models.CharField(max_length=150)),
                ('discount', models.CharField(max_length=150)),
                ('Modified_date', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'Purchased_items_by_importer',
                'managed': False,
            },
        ),
        migrations.AlterModelTable(
            name='endinginventory',
            table='Ending_inventory',
        ),
    ]
