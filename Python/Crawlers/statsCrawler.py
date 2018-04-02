from bs4 import BeautifulSoup
soup = BeautifulSoup("http://www.legavolley.it/Statistiche.asp?TipoStat=1.1&Serie=1&AnnoInizio=2017&Fase=1&Giornata=6180&Squadra=LT", 'html.parser')



for link in soup.find_all('table'):
    print(link.get('href'))