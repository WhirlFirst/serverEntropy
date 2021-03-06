"""entropy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from date import views as date_views
from home import views as home_views
from fomula import views as formula_views
from love import views as love_views
urlpatterns = [
    #(r'^time/$', current_datetime),
    url(r'^$',date_views.date,name='main'),
    url(r'^home$',home_views.home,name='home'),
    url(r'^api/formula/$',formula_views.formula_data,name='formula_data'),
    url(r'^api/date/$',date_views.date_data,name='date_data'),
    url(r'^love$',love_views.love,name='love')
]
