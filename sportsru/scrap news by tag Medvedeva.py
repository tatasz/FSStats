from bs4 import BeautifulSoup
import requests
import lxml
import re
import shutil
import os
import urllib.request
import time
import locale
import datetime
locale.setlocale(category=locale.LC_ALL,
                 locale="Russian")

#>>>
#>>>yesterday = datetime.date.today() - datetime.timedelta(1)
#>>>unix_time= yesterday.strftime("%s")

now = time.time()
while (now > 1496275200):
    #131996651 corresponds to Medvedeva
    url = "https://www.sports.ru/stat/tags/player/lenta/131996651.html?ts=" + str(int(now)) + "&filters[2]=all&filters[3]=news&no_controls=1"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "lxml")
    dates = soup.find_all('span', {'class' : 'date'})
    links = soup.find_all('a', {'class': 'short-text'})
    now -= 24 * 60 * 60
    if len(links) > 0:
        print(str(len(links)) + " " + str(datetime.datetime.utcfromtimestamp(now).strftime('%Y-%m-%d')))
        for j in range(len(links)):
            link = links[j]['href']
            tx = links[j].text
            #print(tx);
            with open('news_list_meda.txt', 'a', encoding='utf-8') as file:
                file.write(link + "; " + tx + "\n")
    else:
        print("0")
        now += 12 * 60 * 60






















