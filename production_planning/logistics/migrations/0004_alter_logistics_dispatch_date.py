# Generated by Django 4.1.4 on 2023-01-17 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0003_rename_finished_product_logistics_used_finished_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logistics',
            name='dispatch_date',
            field=models.DateField(),
        ),
    ]