# Generated by Django 4.1.4 on 2023-01-25 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0006_alter_logistics_n_po'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logistics',
            name='form_of_dispatch',
            field=models.CharField(choices=[('consolidated', 'consolidado'), ('bus', 'micro'), ('withdraw', 'retira')], default='consolidated', max_length=12),
        ),
        migrations.AlterField(
            model_name='logistics',
            name='n_po',
            field=models.CharField(max_length=11),
        ),
    ]
