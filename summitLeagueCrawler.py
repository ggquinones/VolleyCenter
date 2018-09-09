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

def formatSheet(varSheet):
	# Moves totals 2 columns over		
	lastRow = varSheet[-1]
	lastRow.insert(1,' ')
	lastRow.insert(2,' ')
	varSheet[-1] = lastRow
	# Eliminates row with Attack//Serve//Block
	varSheet.pop(1)
	return varSheet

soup = getSoup("http://www.thesummitleague.org/sports/wvball/2017-18/boxscores/20170825_o99i.xml")
sauce = soup.find_all("div",class_="stats-fullbox clearfix")
bs1 = formatSheet(getTeamBoxscore(1,sauce))
bs2 = formatSheet(getTeamBoxscore(2,sauce))
data = OrderedDict()
data.update({"Sheet 1": bs1})
data.update({"Sheet 2": bs2})
save_data("test.ods", data)


