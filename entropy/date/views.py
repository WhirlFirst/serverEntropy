from django.http import HttpResponse
from date.models import Date
from date.models import Processing
from django.shortcuts import render
from django.http import JsonResponse
import datetime
import random
now = datetime.datetime.now().strftime("%m%d")
int(now)
current_time=datetime.datetime.now().strftime("%y.%m.%d")
d=Date.objects.filter(day=now)
d=str(d)
f=d.split("\t")
del f[0]
def date(request):
    d=random.choice(f)
    U=random.choice(Processing.objects.all())
    return render(request,'date.html',locals())
# Create your views here.

def date_data(request):
    seed_day = datetime.datetime.now().strftime("%y%m%d")
    random.seed(seed_day)
    Processing_data= random.choice(Processing.objects.all())
    date_dict = {'thing':random.choice(f),'processing': str(Processing_data)}
    return JsonResponse(date_dict)
