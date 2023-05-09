# Generated by Django 3.2.19 on 2023-05-07 10:46

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0008_remove_itemprice_day_shift'),
        ('Revenue', '0004_auto_20230507_0339'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsale',
            name='Item_type',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='Item_category', chained_model_field='Item_category', default=1, on_delete=django.db.models.deletion.CASCADE, to='setup.itemtype'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newsale',
            name='Item_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.itemcategory'),
        ),
    ]