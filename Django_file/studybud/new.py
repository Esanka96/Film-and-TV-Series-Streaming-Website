import os
import django
from django.db import models
import requests
from bs4 import BeautifulSoup
import os,re,sys
#
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studybud.settings')
# Replace 'your_project_name' with your actual project name
django.setup()

from blog.models import postTable  # Replace 'your_app_name' with the name of your Django app

# Rest of your scraping and data storage code

def sanitize_title(title):
    # Remove characters that are not allowed in Windows file names
    invalid_chars = r'[\/:*?"<>|]'
    title = re.sub(invalid_chars, '_', title)
    return title

def scrape_and_store_data():

    for i in range(1):
        if i==0:
            url = 'https://cinesubz.co/movies/'
        else:
            url='https://cinesubz.co/movies/page/'+str(i+1)+'/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        div_ele = soup.find('div', class_='animation-2 items full')
        article_eles = div_ele.find_all('article', class_='item movies')

        for article_ele in article_eles:
            photo=article_ele.find('div', class_='poster').find('img')['src']
            title = article_ele.find('h3').text
            print(title)
            # photo_title = sanitize_title(title)
            # released_date = article_ele.find('div', class_='data').find('span').text
            # new_res=requests.get(photo)
            # image_file=f'{photo_title}.webp'
            # out_folder="C:/Users/SMTC PVT LTD/Desktop/New folder (5)/studybud/static/images"
            # image_path=os.path.join(out_folder,image_file)
            # with open(image_path, 'wb') as f:
            #     f.write(new_res.content)
            # # Create and save a new postTable object with the scraped data
            # movie = postTable(name=title, date=released_date,photo=f'{photo_title}.webp')
            # movie.save()

# Call the function to initiate the scraping and data storage
scrape_and_store_data()
