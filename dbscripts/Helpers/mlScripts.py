import requests
import re
from bs4 import BeautifulSoup
from pyexcel_ods import save_data
from collections import OrderedDict

# This page has the code to process a BoxScore page from the Summit League

def getSoup(link):
	url = link
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html,'html.parser')
	return soup



def getTeamBoxscore(teamNum,allDivTables):
	currTable = allDivTables[teamNum].find("table") # First table is game overview stuff, Second is Team1 then Team2.
	tableRows = currTable.find_all("tr")
	sheet =[]
	for tr in tableRows:
		td = tr.find_all("td")
		th = tr.find_all("th")
		data = td + th
		row = []
		for cell in data:
			noWeirdSpacing = re.sub("(\s)+[*]"," ",cell.text.strip().encode("utf-8"),0, re.DOTALL)			
			row.append(noWeirdSpacing)		
		sheet.append(row)
	return sheet

def extractTotalsRow(varSheet):
	totalsRow = varSheet[-1]
	totalsRow.pop(0)
	return totalsRow

def extractBoxScoreLinks():
	with open("linksToBoxScores.txt") as f:
		links = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
		links = [x.strip() for x in links] 
		return links

def extractTeam(boxscore):
	return boxscore[0][0]

def isSummitLeagueTeam(boxscore):
	summitLeagueTeamsList = ['Oral Roberts','South Dakota State','North Dakota State','Denver','Omaha','Purdue Fort Wayne','Western Illinois','South Dakota']
	return( extractTeam(boxscore) in summitLeagueTeamsList)

def addToCSV(teamName,totals):
	f=open(teamName+"Organized.txt", "a+")
	line = '\n'.join(totals)
	#line = line[:-1]
	f.write(line)
	f.close()

def processLinks():		
	links = extractBoxScoreLinks()
	ct = 0
	for link in links:
		soup = getSoup(link)
		sauce = soup.find_all("div",class_="stats-fullbox clearfix")
		
		team1BXSC = getTeamBoxscore(1,sauce)
		team2BXSC = getTeamBoxscore(2,sauce)
		if isSummitLeagueTeam(team1BXSC):
			print(extractTeam(team1BXSC))
			print(extractTotalsRow(team1BXSC))
			addToCSV(extractTeam(team1BXSC),extractTotalsRow(team1BXSC))
		
		if isSummitLeagueTeam(team2BXSC):
			print(extractTeam(team2BXSC))
			print(extractTotalsRow(team2BXSC))		
			addToCSV(extractTeam(team2BXSC),extractTotalsRow(team2BXSC))
		print("-------------------------")
		

processLinks()
