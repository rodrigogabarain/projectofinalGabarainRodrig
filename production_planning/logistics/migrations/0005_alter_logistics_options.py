# Generated by Django 4.1.4 on 2023-01-17 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0004_alter_logistics_dispatch_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logistics',
            options={'verbose_name': 'Logistico', 'verbose_name_plural': 'Logisticos'},
        ),
    ]