import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

# selenium 은 자동화 프로그램
browser = webdriver.Chrome()
url = "https://news.naver.com/main/ranking/popularDay.naver"
# 브라우저 페이지 열기
browser.get(url)
time.sleep(3)
soup = BeautifulSoup(browser.page_source,"lxml")
print(soup.find("ul",{"class":"rankingnews_list"}))
list_ul = soup.find("ul",{"class":"rankingnews_list"})
print(list_ul.find_all("li"))
list_li = list_ul.find_all("li")
for li in list_li :
    print("순위 : ",li.find("em",{"class":"list_ranking_num"}).text)
    print("제목 : ",li.find("a",{"class":"list_title nclicks('RBP.rnknws')"}).text)
    print("이미지 : ",li.find("img")["src"])

#print(soup.prettify())
#with open('news.html','w',encoding='utf8') as f :
    #f.write(soup.prettify())
#time.sleep(100)