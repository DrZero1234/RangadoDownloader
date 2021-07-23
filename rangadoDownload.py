#!python3
# RangadoDownload.py - Letölti az összes Rangadó .mp3 fájlt ami 2020-tól lett feltöltve
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import os
from pathlib import Path
from time import sleep
import shutil

"""
rangadóMainPage = 'https://patria.rtvs.sk/clanky/rangado-derby?page='
headers = headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'}


# Rangadó mappa létrehozása
Path('C:\\Users\\PC\\Desktop\\Kristof\\Rangadó').mkdir(
    parents=True, exist_ok=True)
os.chdir('C:\\Users\\PC\\Desktop\\Kristof\\Rangadó\\')


def rangadoDownloader():
    # Fájlenevet nem tartalmazható karakterek listába helyezése
    specCharList = ['<', '>', ':', '"', '/', '\'', '|', '?', '*']
    for i in range(1, 3):
        with requests.get(rangadóMainPage + str(i), headers=headers) as re:
            print('Looking through %s' % rangadóMainPage + str(i))
            re.raise_for_status()
            soup = BeautifulSoup(re.text, 'html.parser')
            sleep(5)
            # A Cikkek elemének megkereésése
            articles = soup.find_all('article', class_='col-12 news-item')
            # Az összes cikkre vonatkozó parancsok
            for article in articles:
                #.txt fájl megnyitása olvasásra
                idChecker = open('IdTracker.txt', 'r')
                #.txt fájl megnyitása az oldal ID-nek hozzáírására
                idTracker = open('IdTracker.txt', 'a')
                # A cikk linkjének meghatározása
                articleLink = 'https://patria.rtvs.sk' + \
                    article.find('a')['href']
                # A cikk azonosítószámának kiszedése a linkből
                articleID = articleLink.split('/')[5]
                # Ha a cikk azonosítószáma nincs benne a már letöltött cikkek azonosítóinak listájában
                if str(articleID) not in idChecker.read().split('\n'):
                    # Firefox megnyitása a teljes source kód megszerzéséhez
                    driver = webdriver.Firefox()
                    print('Connecting to %s....' % articleLink)
                    driver.get(articleLink)
                    articleURL = driver.page_source
                    articleSoup = BeautifulSoup(articleURL, 'html.parser')
                    driver.quit()
                    sleep(5)
                    # Cikk címének kiszedése
                    title = articleSoup.find(
                        'h1', class_='page__title').text.strip()
                    # Cikk létrehozásának dátumát kapjuk meg
                    date = articleSoup.find(
                        'div', class_='article__date-name').text.split('|')[0].strip()
                    # A cikk dátuma  NN.HH.ÉÉÉÉ forámtumban
                    dateForFile = date.split(
                        ' ')[0] + date.split(' ')[1] + date.split(' ')[2]
                    # Csak az év kiemelése
                    year = date.split(' ')[2]
                    # Az mp3 fájlt tartalmazó link megkeresése
                    mp3Link = articleSoup.find(
                        'video', class_='fp-engine')['src']
                    if mp3Link == None:
                        print('Couldnt find the mp3 link....')
                        break
                    # Fájlnév kialakítása
                    newFileName = '[' + str(dateForFile) + \
                        '] ' + str(title) + '.mp3'
                    # Ha a fájlév tartalmaz speciális karaktereket azok a karakterek törölve lesznek mivel fájlenevek nem tartalmazhatnak speciális karaktereket
                    for char in specCharList:
                        if char in newFileName:
                            newFileName = newFileName.replace(char, '')
                    # MP3 fájl létrehozása
                    mp3File = open(os.path.basename(mp3Link), 'wb')
                    if int(year) >= 2021:
                        print('Downloading %s.....' % mp3Link)
                        # MP3-as link lekérése
                        mp3Request = requests.get(mp3Link, headers=headers)
                        # Az MP3-as fájl letöltése
                        mp3Request.raise_for_status()
                        for chunk in mp3Request.iter_content(100000):
                            mp3File.write(chunk)
                        mp3File.close()
                        print('Renaming %s to %s' %
                              (os.path.basename(mp3Link), newFileName))
                        # A letöltött MP3-as fájl átnevezése az előbb megadott fájlformátum alapján
                        shutil.move(f'C:\\Users\\PC\\Desktop\\Kristof\\Rangadó\\{os.path.basename(mp3Link)}',
                                    f'C:\\Users\\PC\\Desktop\\Kristof\\Rangadó\\{newFileName}')
                        print('%s added to IdTracker.txt' % articleID)
                        # Az oldal azonosítószámának hozzáírása a .txt fájlba.
                        idTracker.write(articleID + '\n')
                        idTracker.close()
                        sleep(10)
                    else:
                        print('This podcast was before the year 2021')
    print('All files are downloaded.')

    idChecker.close()


rangadoDownloader()
"""
