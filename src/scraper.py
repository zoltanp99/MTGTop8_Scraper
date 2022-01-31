from bs4 import BeautifulSoup
import requests

url='https://www.mtgtop8.com/archetype?a=504&meta=130&f=EDH'
req = requests.get(url)
content = req.text

soup = BeautifulSoup(content, features="html.parser")

massiveArray = []

for i in soup.find_all('tr', attrs={'class':'hover_tr'}):

    #i appended the href because mtgtop8 formatted their hrefs without the base url
    deckListPageUrl = 'https://www.mtgtop8.com/{href}'.format(href=i.a['href'])
    deckListPageRequest = requests.get(deckListPageUrl)
    deckListPageSoup = BeautifulSoup(deckListPageRequest.content, features='html.parser')

    #extracting every unique card and placing it in a list
    massiveArray.append(deckListPageSoup.find('title').text)
    massiveArray.append(deckListPageSoup.find_all('span', attrs={'class': 'L14'}).text)

text_file = open('Data_Dumps/soup_test_dump.txt', 'w')

for a in massiveArray:
    textRow = 'this should be 1 card:{card}\n'.format(card=a)
    text_file.write(textRow)