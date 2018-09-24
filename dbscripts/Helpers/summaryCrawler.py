import requests
import re
import json
from bs4 import BeautifulSoup
from Match import Match

def getSoup(link):
	url = link
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html,'html.parser')
	return soup
	
def extractTeamOne(mainDiv):
	spans = mainDiv.find_all("span", class_="stats-header")
	team = re.sub( '\s+', ' ', spans[0].text ).strip()
	team = team[0:len(team)-1]
	return team

def extractTeamTwo(mainDiv):
	spans = mainDiv.find_all("span", class_="stats-header")
	team = re.sub( '\s+', ' ', spans[1].text ).strip()
	team = team[0:len(team)-1]
	return team
	
def extractSetsWon(mainDiv):
	spans = mainDiv.find_all("span", class_="stats-header")
	team1 = re.sub( '\s+', ' ', spans[0].text ).strip()
	team2 = re.sub( '\s+', ' ', spans[1].text ).strip()
	setsWon = []
	setsWon.append(team1[-1])
	setsWon.append(team2[-1])
	return setsWon	

def extractTeam1Hitting(mainDiv):
	sheet = []
	tables = mainDiv.find_all("table")
	tableRows = tables[2].find_all("tr")
	
	for tr in tableRows:
		td = tr.find_all("td")
		th = tr.find_all("th")
		data = td + th
		
		row = []
		for cell in data:
			noWeirdSpacing = re.sub("(\s)+[*]"," ",cell.text.strip().encode("utf-8"),0, re.DOTALL)			
			row.append(noWeirdSpacing)		
		sheet.append(row)
	del sheet[0]
	del sheet[0]
	return(sheet)
	
def extractTeam2Hitting(mainDiv):
	sheet = []
	tables = mainDiv.find_all("table")
	tableRows = tables[3].find_all("tr")
	
	for tr in tableRows:
		td = tr.find_all("td")
		th = tr.find_all("th")
		data = td + th
		
		row = []
		for cell in data:
			noWeirdSpacing = re.sub("(\s)+[*]"," ",cell.text.strip().encode("utf-8"),0, re.DOTALL)			
			row.append(noWeirdSpacing)		
		sheet.append(row)
	del sheet[0]
	del sheet[0]
	return(sheet)
	
def makeMatch(mainDiv):
	team1 = extractTeamOne(mainDiv)
	team2 = extractTeamTwo(mainDiv)
	setsWon = extractSetsWon(mainDiv)
	pointDistribution = extractSetScores(mainDiv)
	team1Hitting = extractTeam1Hitting(mainDiv)
	team2Hitting = extractTeam2Hitting(mainDiv)
	newMatch = Match(team1,team2,setsWon,pointDistribution,team1Hitting,team2Hitting)
	toString(newMatch)

def toString(match):
		try:
			print (json.dumps(match.__dict__)+"\n-----------------------")            
		except:
			print("Error turning Record to JSON."+ match.team1 + "vs. "+ match.team2 + "\n")

def extractSetScores(mainDiv):
	sheet = []
	tables = mainDiv.find_all("table")
	tableRows = tables[1].find_all("tr")
	
	for tr in tableRows:
		td = tr.find_all("td")
		data = td 
		row = []
		for cell in data:
			noWeirdSpacing = re.sub("(\s)+[*]"," ",cell.text.strip().encode("utf-8"),0, re.DOTALL)			
			row.append(noWeirdSpacing)		
		sheet.append(row)
	del sheet[0]
	return sheet
		
soup = getSoup("http://www.thesummitleague.org/sports/wvball/2018-19/boxscores/20180824_75zo.xml")
mainDiv = soup.find("div",class_="stats-wrapper clearfix")
makeMatch(mainDiv)


