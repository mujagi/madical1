import requests
from bs4 import BeautifulSoup
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

url = "https://www.daum.net/"

browser = webdriver.Chrome()

browser.get(url)
time.sleep(3)

elem = browser.find_element(By.CLASS_NAME,'btn_login')
time.sleep(3)
elem.click()

input_js = 'document.getElementById("loginId--1").value = "{id}";\
            document.getElementById("password--2").value = "{pw}";\
            '.format(id="0", pw = "0")
time.sleep(random.randint(2,5))

browser.execute_script(input_js)
time.sleep(random.randint(2,5))

elem = browser.find_element(By.CLASS_NAME,'highlight')
elem.click()

time.sleep(100)