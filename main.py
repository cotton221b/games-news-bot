import requests
import telegram
from bs4 import BeautifulSoup
from time import sleep
from dotenv import load_dotenv#
import os
load_dotenv()

# #СОЗДАЕМ КОТА-БОТА
botapi=os.getenv('BOTAPI')
Group_link=os.getenv('GROUP_LINK')
bot = telegram.Bot(token=botapi)

while True:
     # ПОЛУЧАЕМ СТРАНИЦУ САЙТА КОТА
     url=("https://coop-land.ru/news/")
     response = requests.get(url)
     response.raise_for_status()


     # ДОСТАЕМ ИНФОРМАЦИЮ СО СТРАНИЦЫ
     soup = BeautifulSoup(response.text, features="html.parser")

     headline = soup.find('h2', class_='title').text
     description = soup.find('div', class_="preview-text").text
     image_url= soup.find('a', class_="img").find('img')['data-src']
     url_for_chat=soup.find('a',class_='big-link')['href']
     full_image_url=(f'https://coop-land.ru{image_url}')


     # СКАЧИВАЕМ КАРТИНКУ КОТА ИЗ ПОСЛЕДНЕГО ПОСТА
     response = requests.get(full_image_url)
     response.raise_for_status()
     with open('coop-land.jpeg', "wb") as file:
          file.write(response.content)


     # СОБИРАЕМ ПОСТ КОТА
     post=(f'''{headline}
        {description}
        {url_for_chat}''')


     # полуучаем последний собраный пост
     with open("coop-land.txt", "r") as my_file:
          file_contents = my_file.read()

     if post != file_contents:
          bot.send_photo(chat_id='@linkformygroup', photo=open('coop-land.jpeg', 'rb'),caption=post)
          my_text = post
          with open("coop-land.txt", "w") as my_file:
               my_file.write(my_text)

     sleep (10)







     
     url_2=("https://www.igromania.ru/news/")
     response = requests.get(url_2)
     response.raise_for_status()


     soup = BeautifulSoup(response.text, features="html.parser")
     full_block=soup.find('div', class_='ShelfCard_card__GrWrN')
     headline=full_block.find('a', class_='ShelfCard_cardLink__mSxdR').text
     description= full_block.find('div', class_="ShelfCard_cardDescription__Tnd7y")
     url_igromania_news= full_block.find('a', class_="ShelfCard_cardLink__mSxdR" )['href']
     url_igromania_full=(f'https://www.igromania.ru'+url_igromania_news)
     response = requests.get(url_igromania_full)
     response.raise_for_status()
     sup = BeautifulSoup(response.text, features="html.parser")
     image_url= sup.find('div', class_="Zoomable_content__D_3gt").find ('img')['src']
     full_image_url=(f'{image_url}')

     response = requests.get(full_image_url)
     response.raise_for_status()


     with open('igromania.jpeg', 'wb') as handler:
        handler.write(response.content)



     if description == None:

          post = f"{headline}\n{image_url}\n{url_igromania_full}"
     else:
          post = f"{headline}\n{description}\n{image_url}\n{url_igromania_full}"



     with open("igromania.txt", "r") as my_file:
          file_contents = my_file.read()

     if post != file_contents:
          bot.send_photo(chat_id='@linkformygroup', photo=open('igromania.jpeg', 'rb'),caption=post)
          with open("igromania.txt", "w") as my_file:
               my_file.write(post)
     
     sleep (10)