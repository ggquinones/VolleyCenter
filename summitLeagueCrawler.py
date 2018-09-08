import requests
import re
from bs4 import BeautifulSoup

url = "http://www.thesummitleague.org/sports/wvball/2017-18/boxscores/20170825_o99i.xml"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html,'html.parser')
fileLog = open("oralrobertsVspurdue.txt","a")

#for table in soup.find_all("table"):
divs = soup.find_all("div",class_="stats-fullbox clearfix")
table = divs[2].find("table")
tableRows = table.find_all("tr")
for tr in tableRows:
	td = tr.find_all("td")
	row = []
	for cell in td:
		noWeirdSpacing = re.sub("(\s)+[*]"," ",cell.text.strip().encode("utf-8"),0, re.DOTALL)
		fileLog.write(noWeirdSpacing +" ")
	fileLog.write("\n")




