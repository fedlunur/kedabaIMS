# Generated by Django 3.2.19 on 2023-05-06 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_currentuser.db.models.fields
import django_currentuser.middleware
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('setup', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('sales_date', models.DateField(default=django.utils.timezone.now)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.customer')),
                ('updated_by', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='m5', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=11)),
                ('sale_single_price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('sale_total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.productcategory')),
                ('product_type', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='product_category', chained_model_field='product_category', on_delete=django.db.models.deletion.CASCADE, to='setup.producttype')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Revenue.sale')),
            ],
        ),
    ]
