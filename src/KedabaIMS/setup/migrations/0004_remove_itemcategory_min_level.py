# Generated by Django 3.2.19 on 2023-05-06 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0003_itemcategory_min_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemcategory',
            name='min_level',
        ),
    ]
