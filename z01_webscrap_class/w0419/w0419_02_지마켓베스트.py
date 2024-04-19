import requests
from bs4 import BeautifulSoup

url = "https://www.gmarket.co.kr/n/best"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

#print(soup.find("p",{"class":"no1"}).text)
#print(soup.find("a",{"class":"itemname"}).text)
#print(soup.find("div",{"class":"s-price"}).span.next.next.next.next)

#print(soup.findAll("li"))
type_best = soup.find("div",{"class":"best-list"})

# 1개씩 찾기
#li01 =type_best.find("li")
#print("li01 순위 : ",li01.p.text)
#print("li01 제목 : ",li01.find("a",{"class":"itemname"}).text)
#print("li01 가격 : ",li01.find("div",{"class":"s-price"}).strong.span.text)
#------------------------------------------------------------------------

# 내가한거
#print(soup.find("div",{"class":"best-list"}))
#type_li = type_best.findAll("li")
#print(type_li)
#for i in range(4):
#    li = type_li[i]
#    print(li.text.strip())
#---------------------------------------------------------------

# 쌤이 한거
lis =type_best.findAll("li")
print("베스트 상품 개수 : ",len(lis))

for li in lis[0:4] :
    print("순위 :",li.p.text)
    print("제목 :",li.find("a",{"class":"itemname"}).text)
    print("가격 :",li.find("div",{"class":"s-price"}).strong.span.text)
    print("-"*40)