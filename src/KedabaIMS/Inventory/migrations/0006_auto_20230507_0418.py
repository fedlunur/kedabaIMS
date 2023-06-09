# Generated by Django 3.2.19 on 2023-05-07 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('setup', '0008_remove_itemprice_day_shift'),
        ('Inventory', '0005_auto_20230507_0417'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchasedinventory',
            options={'verbose_name_plural': 'Begin inventories'},
        ),
        migrations.RenameField(
            model_name='purchasedinventory',
            old_name='Measurement',
            new_name='Unit',
        ),
        migrations.RenameField(
            model_name='purchasedinventory',
            old_name='Purchased_total_price',
            new_name='purchased_total_price',
        ),
        migrations.RenameField(
            model_name='purchasedinventory',
            old_name='Purchased_single_price',
            new_name='unit_purchased_price',
        ),
        migrations.AddField(
            model_name='purchasedinventory',
            name='batch',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchasedinventory',
            name='discount',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchasedinventory',
            name='expired_date',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchasedinventory',
            name='importer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='setup.importer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchasedinventory',
            name='min_level',
            field=models.PositiveIntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='purchasedinventory',
            name='Modified_by',
            field=django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='m27', to=settings.AUTH_USER_MODEL),
        ),
    ]
