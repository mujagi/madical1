import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

type_table = soup.find("table",{"class":"type_5"})
#print(type_table)
type_tr = type_table.find_all("tr")
#print(type_tr)

#print(type_tr[2])

for i in range(15) :
    type_td=type_tr[i]
    type_td.find_all("td")
    if type_td == 1 :
        continue
    for j in type_td:
        print(j.text.strip())