# Generated by Django 4.1.4 on 2023-01-20 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0008_alter_planner_dispatch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planner',
            name='dispatch',
            field=models.CharField(choices=[('consolidated', 'consolidated'), ('bus', 'bus'), ('withdraw', 'withdraw')], max_length=12),
        ),
    ]
