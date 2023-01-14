from myworldapp.models import usd_rate,aus_rate,jpy_rate
from bs4 import BeautifulSoup
import requests,time


def sayhi():
    print("hi")

def get_current():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" 
               "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
    resp = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW",headers=headers)
    if resp.status_code != 200:
        return None
    else:
        return resp.text

def task_usd(request):
    if request.method == "GET":
        current = get_current()
        soup = BeautifulSoup(current, "html.parser")
        table = soup.find("table", class_="table table-striped table-bordered table-condensed table-hover")
        tbody = table.find("tbody")
        country = tbody.find_all("div", class_="hidden-phone print_show")[0].text.strip()
        sight_in = tbody.find_all("td", class_="rate-content-sight text-right print_hide")[0].text.strip()
        sight_out = tbody.find_all("td", class_="rate-content-sight text-right print_hide")[1].text.strip()
        cash_in = tbody.find_all("td", class_="rate-content-cash text-right print_hide")[0].text.strip()
        cash_out = tbody.find_all("td", class_="rate-content-cash text-right print_hide")[1].text.strip()
        search_date = time.strftime("%Y年%m月%d日")
        search_time = time.strftime("%H點%M分")
        data = usd_rate.objects.create(country=country, sight_in=sight_in, sight_out=sight_out, cash_in=cash_in,
                                       cash_out=cash_out, search_date=search_date, search_time=search_time)
        data.save()

