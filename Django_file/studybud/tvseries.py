import requests
from bs4 import BeautifulSoup
import os,re,sys
import django
from django.db import models

def sanitize_title(title):
    invalid_chars = r'[\/:*?"<>|]'
    title = re.sub(invalid_chars, '_', title)
    return title

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studybud.settings')
django.setup()

from blog.models import TVtable

url='https://cinesubz.co/tvshows/page/3/'

response=requests.get(url)
soup=BeautifulSoup(response.content,'html.parser')
main_div=soup.find('div',class_='animation-2 items full')
articles=main_div.find_all('article',class_='item tvshows')

name_list=[]
date_list=[]
image_list=[]
for article in articles:
    title=article.find('div',class_='data').find('h3').text
    date = article.find('div', class_='data').find('span').text
    print(title)
    list_name,created=TVtable.objects.get_or_create(name=title,date=date)
    title=sanitize_title(title)
    photo_link=article.find('div',class_='poster').find('img').get('src')
    imageres=requests.get(photo_link)
    out_path = "C:/Users/SMTC PVT LTD/Desktop/New folder (5)/studybud/static/images"
    image_path = os.path.join(out_path, f'{title}.webp')

    list_name.photo=image_path
    list_name.save()

    with open(image_path, 'wb') as f:
        f.write(imageres.content)
