import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

#전에 했던것들 = 태그로 찾는 방법 title,get_text(),text,a,attr,a["href"]
# find : 태그정보 찾기 함수, class로 찾는방법
#print(soup.find(attrs={"class":"box_type_l"}))
print(soup.find("tr",{"class":"type1"})) #find,  findall, class 
type_tr = soup.find("tr",{"class":"type1"})
print("th : ",type_tr.th) # 첫번째 th 태그를 찾아줌
print(type_tr.find_all("th")) # 전체 th 태그를 찾아줌 list로 들고옴
ths = type_tr.find_all("th")
for th in ths :
    print("제목 : ",th.text) 