import requests
from bs4 import BeautifulSoup
import csv 

contestList = []
url = "https://clist.by/"

content = requests.get(url)

sites = {"codechef.com","codeforces.com","atcoder.jp","topcoder.com"}

soup = BeautifulSoup(content.text,'html.parser')

maindiv = soup.find("div",{"id":"contests"})

rows = maindiv.find_all("div",{"class":"row contest coming"})

for row in rows:
    site = row.find("small")
    site = site.get_text()
    if(site in sites ):
        reqdiv = row.find("div",{"class":"col-md-7 col-sm-8 event"})
        anchor = reqdiv.find("a")
        contestsName = (anchor['title']).encode("utf-8")
        contestLink = (anchor['href']).encode("utf-8")
        print(contestsName,contestLink)
        contestCell = [contestsName,contestLink]
        contestList.append(contestCell)
        
with open ('C:\Users\Ranjit\Desktop\contests.csv','wb') as file:
    writer = csv.writer(file)
    for row in contestList:
        writer.writerow(row)
