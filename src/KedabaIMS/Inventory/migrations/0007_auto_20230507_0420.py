# Generated by Django 3.2.19 on 2023-05-07 11:20

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Inventory', '0006_auto_20230507_0418'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchasedinventory',
            options={'verbose_name_plural': 'Purchased inventories'},
        ),
        migrations.RenameField(
            model_name='purchasedinventory',
            old_name='Unit',
            new_name='Measurement',
        ),
        migrations.RenameField(
            model_name='purchasedinventory',
            old_name='unit_purchased_price',
            new_name='Purchased_single_price',
        ),
        migrations.RenameField(
            model_name='purchasedinventory',
            old_name='purchased_total_price',
            new_name='Purchased_total_price',
        ),
        migrations.RemoveField(
            model_name='purchasedinventory',
            name='batch',
        ),
        migrations.RemoveField(
            model_name='purchasedinventory',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='purchasedinventory',
            name='expired_date',
        ),
        migrations.RemoveField(
            model_name='purchasedinventory',
            name='importer',
        ),
        migrations.RemoveField(
            model_name='purchasedinventory',
            name='min_level',
        ),
        migrations.AlterField(
            model_name='purchasedinventory',
            name='Modified_by',
            field=django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='m8', to=settings.AUTH_USER_MODEL),
        ),
    ]