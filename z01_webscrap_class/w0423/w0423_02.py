import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

# selenium 으로 정보 가져오기
browser = webdriver.Chrome()
browser.get("https://comic.naver.com/bestChallenge")
time.sleep(3)
soup = BeautifulSoup(browser.page_source,"lxml")

list_ul = soup.find("ul",{"class":"AsideList__content_list--FXDvm AsideList__challenge--HeKuU"})

lis = list_ul.find_all("li")
for li in lis :
    w_rank = li.find("strong",{"class":"AsideList__ranking--sNPZy"}).text
    print("등수 : ",w_rank)
    print("제목 : ", li.find("span",{"class":"text"}).text)
    print("작가 : ", li.find("a",{"class":"ContentAuthor__author--CTAAP"}))
    print("이미지 : ",li.find("img",{"class":"Poster__image--d9XTI"})["src"])
    

