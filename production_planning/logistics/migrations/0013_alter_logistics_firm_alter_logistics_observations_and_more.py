# Generated by Django 4.1.4 on 2023-01-25 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0012_alter_logistics_address_alter_logistics_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logistics',
            name='firm',
            field=models.CharField(max_length=5, verbose_name='Firma'),
        ),
        migrations.AlterField(
            model_name='logistics',
            name='observations',
            field=models.CharField(max_length=1500, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='logistics',
            name='used_finished_product',
            field=models.CharField(max_length=15, verbose_name='Producto terminado'),
        ),
        migrations.AlterField(
            model_name='logistics',
            name='used_finished_product1',
            field=models.BooleanField(default=True, verbose_name='Producto terminado descargado'),
        ),
        migrations.AlterField(
            model_name='logistics',
            name='used_raw_material',
            field=models.CharField(max_length=11, verbose_name='Materia prima'),
        ),
        migrations.AlterField(
            model_name='logistics',
            name='used_raw_material1',
            field=models.BooleanField(default=True, verbose_name='Materia prima descargada'),
        ),
    ]
