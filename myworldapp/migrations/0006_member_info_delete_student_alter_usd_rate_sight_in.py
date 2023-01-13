# Generated by Django 4.1 on 2022-12-19 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myworldapp', '0005_aus_rate_jpy_rate_usd_rate_delete_currency_rate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='member_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mSex', models.CharField(default='M', max_length=2)),
                ('mBirthday', models.DateField()),
                ('mEmail', models.EmailField(blank=True, default='', max_length=100)),
                ('mPassword', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='student',
        ),
        migrations.AlterField(
            model_name='usd_rate',
            name='sight_in',
            field=models.FloatField(default='', max_length=2),
        ),
    ]
