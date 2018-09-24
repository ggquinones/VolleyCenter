import requests
import re
import json
from urllib import urlencode
import urllib2
from bs4 import BeautifulSoup
from Match import Match


def mainRunner(link):
	bxscLinks = getBoxScoreLinks(getSoup(link))
	season = re.search(r'(\d)+-(\d)+',link).group(0)
	gameNumber = 0
	for link in bxscLinks:
		currMatch = Match(getSoup(link).find("div",class_="stats-wrapper clearfix"),season,gameNumber,link)
		matches = json.dumps(currMatch.__dict__)
		headers = {'content-type': 'application/json'}
		#Un-comment this line to send Matches to API route 
		r = requests.post("http://localhost:4000/matches",data=matches,headers=headers)
		gameNumber+=1
		print(matches)
	#print(gameNumber)
		
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

