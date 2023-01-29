# Generated by Django 4.1.4 on 2023-01-23 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operative', '0003_alter_operative_firm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operative',
            name='manufacturing_date',
            field=models.CharField(max_length=8, verbose_name='Fecha mecanizado'),
        ),
        migrations.AlterField(
            model_name='operative',
            name='production_entry_date',
            field=models.CharField(max_length=8, verbose_name='Fecha ingreso Prod.'),
        ),
    ]
