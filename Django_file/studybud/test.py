import os
import django
from django.db import models
import requests
from bs4 import BeautifulSoup
import os,re,sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studybud.settings')

django.setup()
from blog.models import postTable
from blog.models import List
from blog.models import Person
from blog.models import Actor
from blog.models import Filmname
from blog.models import Filmphoto

def sanitize_title(title):
    invalid_chars = r'[\/:*?"<>|]'
    title = re.sub(invalid_chars, '_', title)
    return title

def remove_element(content,element):
    for img in content.find_all(element):
        img.extract()
    return content

def remove_images_and_alt(html_content):
    if html_content:
        html_content['style'] = 'font-family: verdana, geneva, sans-serif; font-size: 13pt; color: #000000;'

    remove_element(html_content,'img')
    remove_element(html_content, 'h3')
    remove_element(html_content, 'ul')
    remove_element(html_content, 'h4')
    return html_content


def scrape_and_store_data():

    for i in range(3):
        if i==0:
            url = 'https://cinesubz.co/movies/'
        else:
            url='https://cinesubz.co/movies/page/'+str(i+1)+'/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        div_ele = soup.find('div', class_='animation-2 items full')
        article_eles = div_ele.find_all('article', class_='item movies')

        for article_ele in article_eles:
            final_url=article_ele.find('div', class_='poster').find('a')['href']
            photo = article_ele.find('div', class_='poster').find('img')['src']
            title = article_ele.find('h3').text
            print(title)
            new_response=requests.get(final_url)
            new_soup=BeautifulSoup(new_response.text,'html.parser')

            associated_items = []
            genre_elements = new_soup.find('div', class_='sgeneros').find_all('a', rel='tag')
            for i in genre_elements:
                list_item,created=List.objects.get_or_create(name=i.text)
                associated_items.append(list_item)

            person_list=[]
            person_element=new_soup.find('div', class_='persons').find_all('div', class_='person')
            for per in person_element:
                act_name=per.find('div', class_='name').text.strip()
                list_item, created=Person.objects.get_or_create(name=act_name)
                person_list.append(list_item)

            actors_list=[]
            person_element=new_soup.find_all('div', class_='persons')[1].find_all('div', class_='person')
            for per in person_element:
                act_name=per.find('div', class_='name').text.strip()
                list_item, created=Actor.objects.get_or_create(name=act_name)
                actors_list.append(list_item)

            film_name_list=[]
            film_name=new_soup.find('span', class_='tagline').text.strip()
            item,created=Filmname.objects.get_or_create(name=film_name)
            film_name_list.append(item)

            film_photo_list = []
            photo_list = new_soup.find_all('img')
            for photoo in photo_list:
                src = photoo.get('src')
                if src.startswith('https://image.tmdb.org/t/p/w300/'):
                    src = src.rstrip('\r')
                    image_name = os.path.basename(src)  # Get the filename from the URL
                    image_name = os.path.splitext(image_name)[0]
                    last_res = requests.get(src)
                    out_path = "C:/Users/SMTC PVT LTD/Desktop/New folder (5)/studybud/static/images"
                    image_path = os.path.join(out_path, f'{image_name}.jpeg')
                    with open(image_path, 'wb') as f:
                        f.write(last_res.content)

                    filmphoto, created = Filmphoto.objects.get_or_create(photo=f'{image_name}.jpeg')  # Assuming 'photo' is a FileField in your model
                    film_photo_list.append(filmphoto)

            span_ele=new_soup.find_all('span', class_='wp-content')[1]
            sanitized_html = remove_images_and_alt(span_ele)
            sanitized_text = sanitized_html.get_text()
            photo_title = sanitize_title(title)
            released_date = article_ele.find('div', class_='data').find('span').text
            new_res=requests.get(photo)
            image_file=f'{photo_title}.webp'
            out_folder="C:/Users/SMTC PVT LTD/Desktop/New folder (5)/studybud/static/images"
            image_path=os.path.join(out_folder,image_file)
            with open(image_path, 'wb') as f:
                f.write(new_res.content)
            movie = postTable(name=title, date=released_date,description=sanitized_text,photo=f'{photo_title}.webp')
            movie.save()
            movie.item.add(*associated_items)
            movie.persons.add(*person_list)
            movie.actros.add(*actors_list)
            movie.filmnames.add(*film_name_list)
            movie.filmphotos.add(*film_photo_list)

scrape_and_store_data()
