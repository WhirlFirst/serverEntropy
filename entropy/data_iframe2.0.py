import os
import re
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "entropy.settings")

import django

django.setup()

def main():
    from date.models import Processing


    sourcefile = open('H:\\netscrapy\\Processing\\processing.txt', 'r')
    processing_original_data = sourcefile.read()
    processing_url = re.compile('href="/sketch/[0-9]+"')
    all_processing_url = processing_url.findall(processing_original_data)
    name1=0
    for url in all_processing_url:
        url = url[6:-1]
        url = "https://www.openprocessing.org/" + url + "/embed/"
        print(url)
        name1=name1+1
        Processing.objects.get_or_create(name=name1,iframe=url)


if __name__ == "__main__":
    main()
    print('Done!')