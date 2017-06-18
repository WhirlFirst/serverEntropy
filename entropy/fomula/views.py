from django.shortcuts import render
from fomula.models import fomulaextent
from django.core import serializers
import random
import json
import datetime
from django.http import HttpResponse,JsonResponse
def formula_data(request):
    seed_day = datetime.datetime.now().strftime("%y%m%d")
    random.seed(seed_day)
    database = random.choice(fomulaextent.objects.values_list('number','description','svg','wikipedia'))
    formula_dict= {'number': database[0],'description':database[1],'svg':database[2],'wikipedia':database[3]}
    print(formula_dict)
    return JsonResponse(formula_dict)
# Create your views here.
