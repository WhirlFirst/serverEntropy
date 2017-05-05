#coding:utf-8
from django.db import models


class fomulaextent(models.Model):
    description = models.CharField(max_length=1000)
    svg = models.CharField(max_length=40000)
    wikipedia = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.number
# Create your models here.
