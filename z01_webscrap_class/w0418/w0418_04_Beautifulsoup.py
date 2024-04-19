import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
hedders = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url)
res.raise_for_status()




soup = BeautifulSoup(res.text,"lxml") # text를 html 파싱
#print(soup.prettify()) #html 소스를 정렬해서 출력

print("<title> :",soup.title) # 태그를 입력하면 찾아줌 
print("<title> text : ",soup.title.text) # 태그의 글자를 가져옴
print("<a> 태그:",soup.a)
print("<a> 태그글자 :",soup.a.text)
print("<a> 속성전체 : ",soup.a.attrs) #속성값 들고오기 = attrs
print("<a>[속성] : ",soup.a["href"]) # 태그의 특정 속성값만 들고오기

#with open("stock2.html","w",encoding="utf8") as f :
#    f.write(soup.prettify())