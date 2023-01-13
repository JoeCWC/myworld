"""myworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myworldapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('django.contrib.auth.urls')),
    path('', views.index,name="index"),
    path('index/', views.index,name="index"),
    path("login/", views.login_request, name="login"),
    path('main/',views.main,name="main"),
    path('get_stock/',views.chose),
    path('currency/',views.currency),
    path('usd_history/',views.usd_history),
    path('aus_history/',views.aus_history),
    path('jpy_history/',views.jpy_history),
    path("register/", views.register_request, name="register"),
    path("line_usd_sightin/",views.line_usd_sightin),
    path("line_usd_sightout/",views.line_usd_sightout),
    path("line_usd_cashin/",views.line_usd_cashin),
    path("line_usd_cashout/",views.line_usd_cashout),
    path("line_aus_sightin/",views.line_aus_sightin),
    path("line_aus_sightout/",views.line_aus_sightout),
    path("line_aus_cashin/",views.line_aus_cashin),
    path("line_aus_cashout/",views.line_aus_cashout),
    path("line_jpy_sightin/",views.line_jpy_sightin),
    path("line_jpy_sightout/",views.line_jpy_sightout),
    path("line_jpy_cashin/",views.line_jpy_cashin),
    path("line_jpy_cashout/",views.line_jpy_cashout),



]
