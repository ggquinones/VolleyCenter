import re
import json

class Match(object):

    
  	def __init__(self, mainDiv,season,gameNumber,link):
		self.season = season
		self.gameNumber = gameNumber
		self.boxscoreLink = link  		
		self.setTopInformation(mainDiv)
		self.setPointDistribution(mainDiv)
		#self.setHittingDistributions(mainDiv)
		      
	def setTopInformation(self,mainDiv):
		spans = mainDiv.find_all("span", class_="stats-header")
		team1 = re.sub( '\s+', ' ', spans[0].text ).strip()
		setsWon = []
		setsWon.append(team1[-1])		
		team1 = team1[0:len(team1)-1]
		team2 = re.sub( '\s+', ' ', spans[1].text ).strip()
		setsWon.append(team2[-1])
		team2 = team2[0:len(team2)-1]		
		self.team1 = team1.strip()
		self.team2 = team2.strip()
		self.sets = setsWon
		
	def setPointDistribution(self,mainDiv):
		sheet = []
		tables = mainDiv.find_all("table")
		tableRows = tables[1].find_all("tr")		
		for tr in tableRows:
			td = tr.find_all("td")
			th = tr.find_all("th")
			data = td + th 
			row = []
			for cell in data:
				noWeirdSpacing = re.sub("(\s)+[*]"," ",cell.text.strip().encode("utf-8"),0, re.DOTALL)			
				row.append(noWeirdSpacing)		
			sheet.append(row)
		#del sheet[0]
		self.pointsHeader  = sheet[0]
		self.team1Points  = sheet[1]
		self.team2Points  = sheet[2]

	def setHittingDistributions(self,mainDiv):
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
		
		self.team1HittingDistribution  = sheet
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
		self.team2HittingDistribution = sheet	
			


