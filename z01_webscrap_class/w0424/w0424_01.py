import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'http://google.com'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')
#page = open('google.html','r',encoding='utf8')
#soup = BeautifulSoup(page,'lxml')
#page.close()
with open("google.html","r",encoding='utf8') as f :
    soup = BeautifulSoup(f,'lxml')


print("타이틀 : ",soup.find('title').text)