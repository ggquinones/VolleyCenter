import requests
import re
from bs4 import BeautifulSoup

# Gets all links for boxscores from 2017 Summit League WVB Season
# Saves them in linksToBoxScores.txt for future scraping
url = 'http://www.thesummitleague.org/sports/wvball/2017-18/schedule'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html,'html.parser')
fileLog = open("linksToBoxScores.txt","w")
for link in soup.find_all('a'):
	
	if 'Box Score' in link.text:
		#print link.attrs['aria-label']
		print ("http://www.thesummitleague.org"+link.get('href'))
		# Uncomment to remake file
		fileLog.write("http://www.thesummitleague.org"+link.get('href')+"\n")

