import requests
import re
import json
from urllib import urlencode
import urllib2
from bs4 import BeautifulSoup
from Match import Match


def mainRunner(link):
	bxscLinks = getBoxScoreLinks(getSoup(link))
	season = re.search('(\d)+-(\d)+',link).group(0)
	for link in bxscLinks:
		currMatch = Match(getSoup(link).find("div",class_="stats-wrapper clearfix"))
		#toString(currMatch)
		#matches = json.dumps(currMatch.__dict__)
		r = http_post("https://acs567-ggquinones.c9users.io/enter/match",currMatch.__dict__)
		#r = requests.post(url ="https://acs567-ggquinones.c9users.io/enter/match", data = matches)
		print(r)
		
def getSoup(link):	
	response = requests.get(link)
	html = response.content
	soup = BeautifulSoup(html,'html.parser')
	return soup
	
def getBoxScoreLinks(soup):	
	links = []
	for link in soup.find_all('a'):		
		if 'Box Score' in link.text:
			links.append("http://www.thesummitleague.org"+link.get('href'))
	return links

def http_post(url, data):
    post = urlencode(data)
    req = urllib2.Request(url, post)
    response = urllib2.urlopen(req)
    return response.read()
	

def toString(match):
		try:
			print (json.dumps(match.__dict__)+"\n-----------------------")            
		except:
			print("Error turning Record to JSON."+ match.team1 + "vs. "+ match.team2 + "\n")	
	
		
mainRunner('http://www.thesummitleague.org/sports/wvball/2018-19/schedule')			

