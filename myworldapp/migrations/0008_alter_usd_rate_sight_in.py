# Generated by Django 4.1 on 2022-12-19 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myworldapp', '0007_alter_usd_rate_sight_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usd_rate',
            name='sight_in',
            field=models.FloatField(default='', max_length=2),
        ),
    ]
