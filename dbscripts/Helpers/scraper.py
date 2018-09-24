import requests
import re
from bs4 import BeautifulSoup

seasons = [
'http://www.thesummitleague.org/sports/wvball/2007-08/schedule',
'http://www.thesummitleague.org/sports/wvball/2008-09/schedule',
'http://www.thesummitleague.org/sports/wvball/2009-10/schedule',
'http://www.thesummitleague.org/sports/wvball/2010-11/schedule',
'http://www.thesummitleague.org/sports/wvball/2011-12/schedule',
'http://www.thesummitleague.org/sports/wvball/2012-13/schedule',
'http://www.thesummitleague.org/sports/wvball/2013-14/schedule',
'http://www.thesummitleague.org/sports/wvball/2014-15/schedule',
'http://www.thesummitleague.org/sports/wvball/2015-16/schedule',
'http://www.thesummitleague.org/sports/wvball/2016-17/schedule',
'http://www.thesummitleague.org/sports/wvball/2017-18/schedule'
]

for url in seasons:
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html,'html.parser')
	years = re.search('(\d)+-(\d)+',url,0, re.DOTALL)
	fileLog = open("summitLeagueData/"+years+"Season.txt","w")
	for link in soup.find_all('a'):		
		if 'Box Score' in link.text:
			print ("http://www.thesummitleague.org"+link.get('href'))
			# Uncomment to remake file
			fileLog.write("http://www.thesummitleague.org"+link.get('href')+"\n")

