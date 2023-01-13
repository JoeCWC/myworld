from django.db import models


class usd_rate(models.Model):
    search_date = models.CharField(max_length=20,default='')
    search_time = models.CharField(max_length=20,default='')
    country = models.CharField(max_length=20,default='')
    sight_in = models.CharField(max_length=2,default='')
    sight_out = models.CharField(max_length=20,default='')
    cash_in = models.CharField(max_length=20,default='')
    cash_out = models.CharField(max_length=20,default='')


class aus_rate(models.Model):
    search_date = models.CharField(max_length=20,default='')
    search_time = models.CharField(max_length=20,default='')
    country = models.CharField(max_length=20,default='')
    sight_in = models.CharField(max_length=20,default='')
    sight_out = models.CharField(max_length=20,default='')
    cash_in = models.CharField(max_length=20,default='')
    cash_out = models.CharField(max_length=20,default='')


class jpy_rate(models.Model):
    search_date = models.CharField(max_length=20,default='')
    search_time = models.CharField(max_length=20,default='')
    country = models.CharField(max_length=20,default='')
    sight_in = models.CharField(max_length=20,default='')
    sight_out = models.CharField(max_length=20,default='')
    cash_in = models.CharField(max_length=20,default='')
    cash_out = models.FloatField(default='')



class stock_record(models.Model):
    opening = models.CharField(max_length=20,default='')
    highest_price = models.CharField(max_length=20,default='')
    lowest_price = models.CharField(max_length=20,default='')
    market_cap = models.CharField(max_length=20,default='')
    PE_ratio = models.CharField(max_length=20,default='')
    dividend_yield = models.CharField(max_length=20,default='')
    CDP = models.CharField(max_length=20,default='')
    week_highest = models.CharField(max_length=20,default='')
    week_lowest = models.CharField(max_length=20,default='')
    def __str__(self):
        return self.opening

class member_info(models.Model):
    mName = models.CharField(max_length=30, null=False, blank=False),
    mSex = models.CharField(max_length=2, default='M', null=False)
    mBirthday = models.DateField(null=False)
    mEmail = models.EmailField(max_length=100, blank=True, default='')
    mPassword = models.CharField(max_length=30, null=False, blank=False)

