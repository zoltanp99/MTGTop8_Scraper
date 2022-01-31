from bs4 import BeautifulSoup
import requests


# TODO: make program more versatile by adding the url as a param
def cardScraper():

    #change the number after 'archetype' to the selected one to change which commander is scraped
    url='https://www.mtgtop8.com/archetype?a=504&meta=130&f=EDH'
    req = requests.get(url)
    content = req.text

    soup = BeautifulSoup(content, features="html.parser")

    uniqueCards = set()
    archetypeName = soup.find('title').text.replace('decklists @ mtgtop8.com', '')
    for i in soup.find_all('tr', attrs={'class':'hover_tr'}):

        #i appended the href because mtgtop8 formatted their hrefs without the base url
        deckListPageUrl = 'https://www.mtgtop8.com/{href}'.format(href=i.a['href'])
        deckListPageRequest = requests.get(deckListPageUrl)
        deckListPageSoup = BeautifulSoup(deckListPageRequest.content, features='html.parser')

        #extracting every unique card and placing it in the set
        for j in deckListPageSoup.find_all('span', attrs={'class': 'L14'}):
            uniqueCards.add(j.text + '\n')

    with open('Data_Dumps/uniqueCards.txt', 'w') as text_file:
        text_file.write(f'ALL UNIQUE CARDS IN {archetypeName}\n\n')
        text_file.writelines(uniqueCards)

if __name__ == '__main__':
    # call the function directly if file is accessed as a script
    cardScraper()