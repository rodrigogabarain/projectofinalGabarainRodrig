# Generated by Django 4.1.4 on 2023-01-28 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operative', '0009_alter_operative_manufacturing_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operative',
            old_name='unloading_finished_product',
            new_name='mp_mm',
        ),
        migrations.RenameField(
            model_name='operative',
            old_name='unloading_raw_material',
            new_name='pt_mm',
        ),
    ]
