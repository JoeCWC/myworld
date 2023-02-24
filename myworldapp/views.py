from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db.models import Max, Min
from myworldapp.models import usd_rate,aus_rate,jpy_rate
from myworldapp.forms import NewUserForm
from bs4 import BeautifulSoup
import requests,time


def index(request):
  return render(request,"index.html",locals())

def main(request):
	return render(request,"main.html",locals())

def login_request(request): #登入功能
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def register_request(request): #註冊功能
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			messages.success(request, "Registration successful." )
			return redirect("main")
		else:
			messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def logout(request): #登出
	return redirect("index")

def chose(request): #選擇股價
	if request.method =="POST":
		choice = request.POST['choice']
		URL = "https://www.google.com/search?q="
		if choice == "1":
			stock_id = "2412"
			message = "今日中華電信股價"
			page = get_stock(URL, stock_id)
			stock = get_stock_info(page)
		elif choice == "2":
			stock_id = "2330"
			message = "今日台積電股價"
			page = get_stock(URL, stock_id)
			stock = get_stock_info(page)
		elif choice == "3":
			stock_id = "2454"
			message = "今日聯發科股價"
			page = get_stock(URL, stock_id)
			stock = get_stock_info(page)
		elif choice == "4":
			stock_id = "2881"
			message = "今日富邦金股價"
			page = get_stock(URL, stock_id)
			stock = get_stock_info(page)
		else:
			message = "無此選項,請重新輸入"

	return render(request,"get_stock.html",locals())

def get_stock(url, stock_id): #抓取股價網頁
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
							 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'} #瀏覽器header
	resp = requests.get(url + stock_id, headers=headers)
	if resp.status_code != 200:
		#print("Invalid url:", resp.url)
		return None
	else:
		return resp.text


def get_stock_info(webtxt): #股價爬蟲
	soup = BeautifulSoup(webtxt, "html.parser")
	stock = dict()
	section = soup.find_all("g-card-section")
	# print(section)
	for x in section[3].find_all("table"):
		for y in x.find_all('tr')[:3]:
			key = y.find_all('td')[0].text.strip()
			value = y.find_all('td')[1].text.strip()
			stock[key] = value
	return stock

def currency(request): #匯率爬蟲
	if 'usd' in request.GET:
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
		message = "查詢成功"
		data = usd_rate.objects.create(country=country,sight_in=sight_in,sight_out=sight_out,cash_in=cash_in,
									   cash_out=cash_out,search_date=search_date,search_time=search_time)
		data.save()

	elif 'aus' in request.GET:
		current = get_current()
		soup = BeautifulSoup(current, "html.parser")
		table = soup.find("table", class_="table table-striped table-bordered table-condensed table-hover")
		tbody = table.find("tbody")
		country = tbody.find_all("div", class_="hidden-phone print_show")[3].text.strip()
		sight_in = tbody.find_all("td", class_="rate-content-sight text-right print_hide")[6].text.strip()
		sight_out = tbody.find_all("td", class_="rate-content-sight text-right print_hide")[7].text.strip()
		cash_in = tbody.find_all("td", class_="rate-content-cash text-right print_hide")[6].text.strip()
		cash_out = tbody.find_all("td", class_="rate-content-cash text-right print_hide")[7].text.strip()
		search_date = time.strftime("%Y年%m月%d日")
		search_time = time.strftime("%H點%M分")
		message = "查詢成功"
		data = aus_rate.objects.create(country=country, sight_in=sight_in, sight_out=sight_out, cash_in=cash_in,
									   cash_out=cash_out, search_date=search_date, search_time=search_time)
		data.save()

	elif 'jpy' in request.GET:
		current = get_current()
		soup = BeautifulSoup(current, "html.parser")
		table = soup.find("table", class_="table table-striped table-bordered table-condensed table-hover")
		tbody = table.find("tbody")
		country = tbody.find_all("div", class_="hidden-phone print_show")[7].text.strip()
		sight_in = tbody.find_all("td", class_="rate-content-sight text-right print_hide")[14].text.strip()
		sight_out = tbody.find_all("td", class_="rate-content-sight text-right print_hide")[15].text.strip()
		cash_in = tbody.find_all("td", class_="rate-content-cash text-right print_hide")[14].text.strip()
		cash_out = tbody.find_all("td", class_="rate-content-cash text-right print_hide")[15].text.strip()
		search_date = time.strftime("%Y年%m月%d日")
		search_time = time.strftime("%H點%M分")
		message = "查詢成功"
		data = jpy_rate.objects.create(country=country, sight_in=sight_in, sight_out=sight_out, cash_in=cash_in,
									   cash_out=cash_out, search_date=search_date, search_time=search_time)
		data.save()
	return render(request,"currency.html",locals())

def get_current(): #抓取匯率網頁
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" 
               "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
    resp = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW",headers=headers)
    if resp.status_code != 200:
        #print("Invalid")
        return None
    else:
        return resp.text

def usd_history(request): #呈現美金匯率資料
	data = usd_rate.objects.all()
	max_sightin = usd_rate.objects.aggregate(Max('sight_in'))
	min_sightin = usd_rate.objects.aggregate(Min('sight_in'))
	max_sightout = usd_rate.objects.aggregate(Max('sight_out'))
	min_sightout = usd_rate.objects.aggregate(Min('sight_out'))
	max_cashin = usd_rate.objects.aggregate(Max('cash_in'))
	min_cashin = usd_rate.objects.aggregate(Min('cash_in'))
	max_cashout = usd_rate.objects.aggregate(Max('cash_out'))
	min_cashout = usd_rate.objects.aggregate(Min('cash_out'))
	return render(request,"usd_history.html",locals())

def aus_history(request): #呈現澳幣匯率資料
	data = aus_rate.objects.all()
	max_sightin = aus_rate.objects.aggregate(Max('sight_in'))
	min_sightin = aus_rate.objects.aggregate(Min('sight_in'))
	max_sightout = aus_rate.objects.aggregate(Max('sight_out'))
	min_sightout = aus_rate.objects.aggregate(Min('sight_out'))
	max_cashin = aus_rate.objects.aggregate(Max('cash_in'))
	min_cashin = aus_rate.objects.aggregate(Min('cash_in'))
	max_cashout = aus_rate.objects.aggregate(Max('cash_out'))
	min_cashout = aus_rate.objects.aggregate(Min('cash_out'))
	return render(request,"aus_history.html",locals())

def jpy_history(request): #呈現日圓匯率資料
	data = jpy_rate.objects.all()
	max_sightin = jpy_rate.objects.aggregate(Max('sight_in'))
	min_sightin = jpy_rate.objects.aggregate(Min('sight_in'))
	max_sightout = jpy_rate.objects.aggregate(Max('sight_out'))
	min_sightout = jpy_rate.objects.aggregate(Min('sight_out'))
	max_cashin = jpy_rate.objects.aggregate(Max('cash_in'))
	min_cashin = jpy_rate.objects.aggregate(Min('cash_in'))
	max_cashout = jpy_rate.objects.aggregate(Max('cash_out'))
	min_cashout = jpy_rate.objects.aggregate(Min('cash_out'))
	return render(request,"jpy_history.html",locals())

def line_usd_sightin(request): #美金資料折線圖
	data = usd_rate.objects.all()
	message = "美金走勢 - 即期買入"
	sight_in = usd_rate.objects.values_list('sight_in',flat=True)
	search_date = usd_rate.objects.values_list('search_date',flat=True)
	labels = []
	data2 = []
	for x in search_date:
		labels += [x]
	for y in sight_in:
		data2 += [y]
	context = {
		"labels": labels,
		"data": data2,
	}
	return render(request,"line_usd_sightin.html",locals())

def line_usd_sightout(request): #美金資料折線圖
	data = usd_rate.objects.all()
	message = "美金走勢 - 即期賣出"
	sight_out = usd_rate.objects.values_list('sight_out',flat=True)
	search_date = usd_rate.objects.values_list('search_date',flat=True)
	labels = []
	data2 = []
	for x in search_date:
		labels += [x]
	for y in sight_out:
		data2 += [y]
	context = {
		"labels": labels,
		"data": data2,
	}
	return render(request,"line_usd_sightout.html",locals())

def line_usd_cashin(request): #美金資料折線圖
	data = usd_rate.objects.all()
	message = "美金走勢 - 現金買入"
	cash_in = usd_rate.objects.values_list('cash_in',flat=True)
	search_date = usd_rate.objects.values_list('search_date',flat=True)
	labels = []
	data2 = []
	for x in search_date:
		labels += [x]
	for y in cash_in:
		data2 += [y]
	context = {
		"labels": labels,
		"data": data2,
	}
	return render(request,"line_usd_cashin.html",locals())

def line_usd_cashout(request): #美金資料折線圖
	data = usd_rate.objects.all()
	message = "美金走勢 - 現金賣出"
	cash_out = usd_rate.objects.values_list('cash_out',flat=True)
	search_date = usd_rate.objects.values_list('search_date',flat=True)
	labels = []
	data2 = []
	for x in search_date:
		labels += [x]
	for y in cash_out:
		data2 += [y]
	context = {
		"labels": labels,
		"data": data2,
	}
	return render(request,"line_usd_cashout.html",locals())


def line_aus_sightin(request): #澳幣資料折線圖
	data = aus_rate.objects.all()
	message = "澳幣走勢 - 即期買入"
	sight_in = aus_rate.objects.values_list('sight_in',flat=True)
	search_date = aus_rate.objects.values_list('search_date',flat=True)
	labels = []
	data2 = []
	for x in search_date:
		labels += [x]
	for y in sight_in:
		data2 += [y]
	context = {
		"labels": labels,
		"data": data2,
	}
	return render(request,"line_aus_sightin.html",locals())

def line_aus_sightout(request): #澳幣資料折線圖
	data = aus_rate.objects.all()
	message = "澳幣走勢 - 即期賣出"
	sight_out = aus_rate.objects.values_list('sight_out',flat=True)
	search_date = aus_rate.objects.values_list('search_date',flat=True)
	labels = []
	data2 = []
	for x in search_date:
		labels += [x]
	for y in sight_out:
		data2 += [y]
	context = {
		"labels": labels,
		"data": data2,
	}
	return render(request,"line_aus_sightout.html",locals())

def line_aus_cashin(request): #澳幣資料折線圖
	data = aus_rate.objects.all()
	message = "澳幣走勢 - 現金買入"
	cash_in = aus_rate.objects.values_list('cash_in',flat=True)
	search_date = aus_rate.objects.values_list('search_date',flat=True)
	labels = []
	data2 = []
	for x in search_date:
		labels += [x]
	for y in cash_in:
		data2 += [y]
	context = {
		"labels": labels,
		"data": data2,
	}
	return render(request,"line_aus_cashin.html",locals())

def line_aus_cashout(request): #澳幣資料折線圖
	data = aus_rate.objects.all()
	message = "澳幣走勢 - 現金賣出"
	cash_out = aus_rate.objects.values_list('cash_out',flat=True)
	search_date = aus_rate.objects.values_list('search_date',flat=True)
	labels = []
	data2 = []
	for x in search_date:
		labels += [x]
	for y in cash_out:
		data2 += [y]
	context = {
		"labels": labels,
		"data": data2,
	}
	return render(request,"line_aus_cashout.html",locals())



def line_jpy_sightin(request): #日圓資料折線圖
	data = jpy_rate.objects.all()
	message = "日圓走勢 - 即期買入"
	sight_in = jpy_rate.objects.values_list('sight_in',flat=True)
	search_date = jpy_rate.objects.values_list('search_date',flat=True)
	labels = []
	data2 = []
	for x in search_date:
		labels += [x]
	for y in sight_in:
		data2 += [y]
	context = {
		"labels": labels,
		"data": data2,
	}
	return render(request,"line_jpy_sightin.html",locals())

def line_jpy_sightout(request): #日圓資料折線圖
	data = jpy_rate.objects.all()
	message = "日圓走勢 - 即期賣出"
	sight_out = jpy_rate.objects.values_list('sight_out',flat=True)
	search_date = jpy_rate.objects.values_list('search_date',flat=True)
	labels = []
	data2 = []
	for x in search_date:
		labels += [x]
	for y in sight_out:
		data2 += [y]
	context = {
		"labels": labels,
		"data": data2,
	}
	return render(request,"line_jpy_sightout.html",locals())

def line_jpy_cashin(request): #日圓資料折線圖
	data = jpy_rate.objects.all()
	message = "日圓走勢 - 現金買入"
	cash_in = jpy_rate.objects.values_list('cash_in',flat=True)
	search_date = jpy_rate.objects.values_list('search_date',flat=True)
	labels = []
	data2 = []
	for x in search_date:
		labels += [x]
	for y in cash_in:
		data2 += [y]
	context = {
		"labels": labels,
		"data": data2,
	}
	return render(request,"line_jpy_cashin.html",locals())

def line_jpy_cashout(request): #日圓資料折線圖
	data = jpy_rate.objects.all()
	message = "日圓走勢 - 現金賣出"
	cash_out = jpy_rate.objects.values_list('cash_out',flat=True)
	search_date = jpy_rate.objects.values_list('search_date',flat=True)
	labels = []
	data2 = []
	for x in search_date:
		labels += [x]
	for y in cash_out:
		data2 += [y]
	context = {
		"labels": labels,
		"data": data2,
	}
	return render(request,"line_jpy_cashout.html",locals())











