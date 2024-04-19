import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
#print(soup.find("table",{"class":"type_5"}))
type_table = soup.find("table",{"class":"type_5"})
#print(type_table.find_all("tr"))
type_tr = type_table.find_all("tr")
type_td = type_tr[2].find_all("td")
for td in type_td :
    print(td.text.strip())
