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

def getSummaryTables(teamNum,allDivTables,team1Sum,team2Sum):
	#extract as method later getGameOverview()
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
	
	team1Table = team1Sum[0].find("table") # First table is game overview stuff, Second is Team1 then Team2.
	tableRows = team1Table.find_all("tr")
	
	for tr in tableRows:
		td = tr.find_all("td")
		th = tr.find_all("th")
		data = td + th
		row = []
		for cell in data:
			noWeirdSpacing = re.sub("(\s)+[*]"," ",cell.text.strip().encode("utf-8"),0, re.DOTALL)			
			row.append(noWeirdSpacing)		
		sheet.append(row)
		
	team2Table = team2Sum[0].find("table") # First table is game overview stuff, Second is Team1 then Team2.
	tableRows = team2Table.find_all("tr")
	
	for tr in tableRows:
		td = tr.find_all("td")
		th = tr.find_all("th")
		data = td + th
		row = []
		for cell in data:
			noWeirdSpacing = re.sub("(\s)+[*]"," ",cell.text.strip().encode("utf-8"),0, re.DOTALL)			
			row.append(noWeirdSpacing)		
		sheet.append(row)
		
	
	
	
	##
	return sheet

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

def formatSheet(varSheet):
	# Moves totals 2 columns over		
	lastRow = varSheet[-1]
	lastRow.insert(1,' ')
	lastRow.insert(2,' ')
	varSheet[-1] = lastRow
	# Eliminates row with Attack//Serve//Block
	varSheet.pop(1)
	return varSheet

def extractBoxScoreLinks():
	with open("linksToBoxScores.txt") as f:
		links = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
		links = [x.strip() for x in links] 
		return links

def processLinks():		
	links = extractBoxScoreLinks()
	ct = 0
	for link in links:
		soup = getSoup(link)
		sauce = soup.find_all("div",class_="stats-fullbox clearfix")
		team1Summary = soup.find_all("div",class_="stats-halfbox-left")
		team2Summary = soup.find_all("div",class_="stats-halfbox-right")
		#ss = getSummaryTables(0,sauce,team1Summary,team2Summary)
		bs1 = formatSheet(getTeamBoxscore(1,sauce))
		bs2 = formatSheet(getTeamBoxscore(2,sauce))
		print(bs1[-1])
		print(bs2[-1])
		print("-------------------------")
		#data = OrderedDict()
		#data.update({"Sheet 1": ss})
		#data.update({"Sheet 2": bs1})
		#data.update({"Sheet 3": bs2})
		
		#save_data("game"+str(ct)+".ods", data)
		#ct += 1

processLinks()
