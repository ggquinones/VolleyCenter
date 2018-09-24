import requests
import re
from bs4 import BeautifulSoup

url = "http://www.thesummitleague.org/sports/wvball/2017-18/boxscores/20170825_o99i.xml"
response = requests.get(url)
html = response.content

def getAwayTeamPerSetKillAttackStats(soup):
	return soup.find_all("table")[3].text;
	
def getAwayTeamIndividualStats(soup):
	return soup.find_all("table")[4].text;
	
def getgetHomeIndividualStats(soup):
	return soup.find_all("table")[5].text;
	
def getgetHomePerSetKillAttackStats(soup):
	return soup.find_all("table")[2].text;

def getSetRecaps(soup):
	link = soup.find_all("table")[1].text
	return link


def getFinalSetsScore(soup):	
	finalAnswer = ""
	for link in soup.find_all("span","stats-header"):
		noMultiWhiteSpaces = re.sub("(\s)+"," ",link.text,0,re.DOTALL)
		noNewLines = re.sub("\n"," ",noMultiWhiteSpaces.strip(),0, re.DOTALL)
		finalAnswer += noNewLines + " "
	return finalAnswer

soup = BeautifulSoup(html,'html.parser')
fileLog = open("oralrobertsVspurdue.txt","w")
 
for link in soup.find_all("span","stats-header"):
		word = link.text
		for char in word:			
			if ord(char) == 32 or ord(char) == 255:
				word = word.replace(char,"")
			elif ord(char) == 10:
				word = word.replace(char," ")
		print(word)

#print(getFinalSetsScore(soup))
#print(getSetRecaps(soup))
#print(getOralRobertsPerSetKillAttackStats(soup)) #player1 in all cases maybe?
#print(getPurduePerSetKillAttackStats(soup)) #player2 in all cases maybe?
print("---------------------------------------------------------------------")

#print(soup.find_all("table")[7])
