#서울 특별시 , 인천광역시, 경기도 3개의 인구를 웹스크래핑 해서
# 서울 특별시 : 인구
# 인천광역시 : 인구 
# 경기도 : 인구 
# 합계 :
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

# selenium 은 자동화 프로그램
browser = webdriver.Chrome()
url = "https://jumin.mois.go.kr/ageStatMonth.do"
# 브라우저 페이지 열기
browser.get(url)
time.sleep(3)
soup = BeautifulSoup(browser.page_source,"lxml")
#print(soup.find("table",{"class":"tbl_type1"}))
tb = soup.find("table",{"class":"tbl_type1"}).tbody
#print(main)

trs = tb.find_all("tr")
s_tds = trs[1].find_all("td")
i_tds = trs[4].find_all("td")
k_tds = trs[9].find_all("td")

print('서울특별시 : ',s_tds[2].text)  
print('인천광역시 : ',i_tds[2].text)  
print('경기도 : ',k_tds[2].text)
s=int(s_tds[2].text.replace(',',''))
i=int(i_tds[2].text.replace(',',''))
k=int(k_tds[2].text.replace(',',''))
total = s+i+k
print('합계 : ',format(total,','))





