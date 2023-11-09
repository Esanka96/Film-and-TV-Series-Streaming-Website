import requests
from bs4 import BeautifulSoup
import os
import django
import re
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studybud.settings')

url='https://cinesubz.co/movies/omg-2-2023-sinhala-subtitles/'
django.setup()
from blog.models import Filmphoto

def sanitize_title(title):
    invalid_chars = r'[\/:*?"<>|]'
    title = re.sub(invalid_chars, '_', title)
    return title

response=requests.get(url)
new_soup=BeautifulSoup(response.text,'html.parser')
film_photo_list = []
photo_list = new_soup.find_all('img')
for photo in photo_list:
    src = photo.get('src')
    if src.startswith('https://image.tmdb.org/t/p/w300/'):
        src=src.rstrip('\r')
        image_name = os.path.basename(src)  # Get the filename from the URL
        image_name = os.path.splitext(image_name)[0]
        last_res = requests.get(src)
        out_path="C:/Users/SMTC PVT LTD/Desktop/New folder (5)/studybud/static/images"
        image_path = os.path.join(out_path, f'{image_name}.jpeg')
        with open(image_path, 'wb') as f:
            f.write(last_res.content)

        filmphoto, created = Filmphoto.objects.get_or_create(photo=sanitize_title(image_path))  # Assuming 'photo' is a FileField in your model
        film_photo_list.append(filmphoto)


        # list_item,created=Filmphoto.objects.get_or_create(photo=src)
        # film_photo_list.append(list_item)
