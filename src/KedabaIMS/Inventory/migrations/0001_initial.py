# Generated by Django 3.2.19 on 2023-05-06 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('setup', '0003_itemcategory_min_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchasedInventory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Quantity', models.PositiveIntegerField()),
                ('Purchased_single_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Purchased_total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('Remark', models.CharField(blank=True, max_length=250, null=True)),
                ('Created_date', models.DateField(auto_now=True)),
                ('Modified_date', models.DateTimeField(auto_now=True)),
                ('Created_by', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Item_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.itemcategory')),
                ('Item_type', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='Item_category', chained_model_field='Item_category', on_delete=django.db.models.deletion.CASCADE, to='setup.itemtype')),
                ('Measurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.measurement')),
                ('Modified_by', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='m8', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Purchased inventories',
            },
        ),
        migrations.CreateModel(
            name='BeginInventory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Quantity', models.PositiveIntegerField()),
                ('purchased_total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('unit_purchased_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('batch', models.CharField(max_length=200)),
                ('expired_date', models.DateField()),
                ('discount', models.FloatField()),
                ('Remark', models.CharField(blank=True, max_length=250, null=True)),
                ('Created_date', models.DateField(auto_now=True)),
                ('Modified_date', models.DateTimeField(auto_now=True)),
                ('Created_by', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Item_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.itemcategory')),
                ('Item_type', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='Item_category', chained_model_field='Item_category', on_delete=django.db.models.deletion.CASCADE, to='setup.itemtype')),
                ('Modified_by', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='m7', to=settings.AUTH_USER_MODEL)),
                ('Unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.measurement')),
                ('importer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.importer')),
            ],
            options={
                'verbose_name_plural': 'Begin inventories',
            },
        ),
    ]
