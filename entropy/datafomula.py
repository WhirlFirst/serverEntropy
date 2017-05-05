import django
import os
import re
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "entropy.settings")
django.setup()

def main():
    from fomula.models import fomulaextent
    filepath = "D:\\fumula"
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        num = allDir
        datapath = "D:\\fumula\\"+ allDir + "\\"
        f=open(datapath+"description.txt",'r')
        descript = f.read()
        descript = re.sub(r'\<.*\>',"",descript)
        svg = open(datapath+"s.html",'r')
        svg = svg.read()
        wiki = open(datapath+"wikipedia.txt",'r')
        wiki = wiki.read()
        fomulaextent.objects.get_or_create(number = num,description = descript,svg = svg,wikipedia = wiki)



if __name__ == "__main__":
    main()
    print('Done!')