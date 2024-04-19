import requests
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
#url = "https://www.coupang.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

#print(len(soup.find("ul",{"class","search-product-list"}).findAll("li")))
ul_search = soup.find("ul",{"class","search-product-list"})
#모든 상품 검색
lis = ul_search.find_all("li")
#print("리스트 개수 : ",len(lis))

for i,li in enumerate(lis[0:20]) :
    #광고상품 제외
    if 'search-product__ad-badge' in li["class"]:
        continue
    
    # 평점 5.0 이상 - 문자와 숫자 비교 에러 
    if float(li.find("span",{"class":"star"}).text) <5.0 :
        continue
    # 평가인원수가 200명 이상 - 정수형으로변경
    if int(li.find("span",{"class":"rating-total-count"}).text[1:-1])<200 :
        continue
    
    print("[",i+1,"번째 상품]")
    print("li class : ",li["class"])
    # 왼쪽, 오른쪽 공백 제거
    print("제목 : ",li.find("div",{"class":"name"}).text.strip())    
    print("가격 : ",li.find("strong",{"class":"price-value"}).text)    
    print("평점 : ",li.find("span",{"class":"star"}).text)    
    print("평점수 : ",li.find("span",{"class":"rating-total-count"}).text)    
    #평가인원수 200명 이상 출력하시오
    print("평점수 : ",li.find("span",{"class":"rating-total-count"}).text[1:-1])