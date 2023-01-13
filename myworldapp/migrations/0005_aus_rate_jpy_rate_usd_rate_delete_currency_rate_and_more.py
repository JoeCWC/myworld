# Generated by Django 4.1 on 2022-12-10 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myworldapp', '0004_rename_nowdate_currency_rate_search_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='aus_rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_date', models.CharField(default='', max_length=20)),
                ('search_time', models.CharField(default='', max_length=20)),
                ('country', models.CharField(default='', max_length=20)),
                ('sight_in', models.CharField(default='', max_length=20)),
                ('sight_out', models.CharField(default='', max_length=20)),
                ('cash_in', models.CharField(default='', max_length=20)),
                ('cash_out', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='jpy_rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_date', models.CharField(default='', max_length=20)),
                ('search_time', models.CharField(default='', max_length=20)),
                ('country', models.CharField(default='', max_length=20)),
                ('sight_in', models.CharField(default='', max_length=20)),
                ('sight_out', models.CharField(default='', max_length=20)),
                ('cash_in', models.CharField(default='', max_length=20)),
                ('cash_out', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='usd_rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_date', models.CharField(default='', max_length=20)),
                ('search_time', models.CharField(default='', max_length=20)),
                ('country', models.CharField(default='', max_length=20)),
                ('sight_in', models.CharField(default='', max_length=20)),
                ('sight_out', models.CharField(default='', max_length=20)),
                ('cash_in', models.CharField(default='', max_length=20)),
                ('cash_out', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='currency_rate',
        ),
        migrations.AddField(
            model_name='stock_record',
            name='CDP',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='stock_record',
            name='PE_ratio',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='stock_record',
            name='dividend_yield',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='stock_record',
            name='highest_price',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='stock_record',
            name='lowest_price',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='stock_record',
            name='market_cap',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='stock_record',
            name='opening',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='stock_record',
            name='week_highest',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='stock_record',
            name='week_lowest',
            field=models.CharField(default='', max_length=20),
        ),
    ]