# Generated by Django 4.1.4 on 2023-01-25 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0009_alter_logistics_form_of_dispatch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logistics',
            name='form_of_dispatch',
            field=models.CharField(choices=[('consolidated', 'consolidado'), ('bus', 'micro'), ('withdraw', 'retira')], max_length=12),
        ),
    ]