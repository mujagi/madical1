import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

type_tr = soup.find("tr",{"class":"type1"})
print("find_next_sibling : ",type_tr.th.find_next_sibling("th")) # 현재 th 에서 다음 th를 찾아줘 
print("next : ",type_tr.th.next) # th 태그 다음 ex (<th>순위</th> => 순위 .next =></th>)

