from django.shortcuts import render
from fomula.models import fomulaextent
import random
import json
from django.http import HttpResponse
def fomula(request,state):
    if state == 'fomula':
        return HttpResponse(json.dumps(random.choice(fomulaextent.objects.all())))
    else:
        return HttpResponse('fail!')
# Create your views here.
