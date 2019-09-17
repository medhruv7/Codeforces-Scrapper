import requests
from bs4 import BeautifulSoup

user = raw_input("Enter your Codeforces ID\n")

user = user.replace(" ","")

url = "https://codeforces.com/submissions/"

url = url+user


print(url)

content = requests.get(url)

soup = BeautifulSoup(content.text,'html.parser')

table = soup.find('table',{"class" : "status-frame-datatable"})

rows = table.find_all('tr')


ok = True

for row in rows:
    data = row.find_all('td')
    
    if(len(data) > 0):
        if((data[0].get_text(strip = True)).encode('utf-8') == "No items"):
            print("No Data To Display")
            ok = False
            break
        problem = (data[3].get_text(strip = True)).encode('utf-8')
        verdict = (data[5].get_text(strip = True)).encode('utf-8')
        datetime = (data[1].get_text(strip = True)).encode('utf-8')
        # print(verdict)
        if(verdict == "Accepted"):
            print(datetime,problem)
