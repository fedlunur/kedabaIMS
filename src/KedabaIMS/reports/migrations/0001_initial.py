# Generated by Django 3.2.19 on 2023-05-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailySaleReport',
            fields=[
                ('id', models.CharField(max_length=150, primary_key=True, serialize=False, unique=True)),
                ('sale_total_price', models.CharField(max_length=250)),
                ('sales_date', models.DateField()),
            ],
            options={
                'db_table': 'gsale',
                'managed': False,
            },
        ),
    ]