from django.test import TestCase
from fomula.models import fomulaextent
import random
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "entropy.settings")
django.setup()
d = random.choice(fomulaextent.objects.all())
print(d)
# Create your tests here.
