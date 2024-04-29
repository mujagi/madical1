import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 화면이 나타나는 것을 확인
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
url = "https://flight.naver.com/"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

time.sleep(1)
# 도착지 선택 // 전체문서
elem = browser.find_element(By.XPATH,'//b[text()="ICN"]')
time.sleep(1)
elem.click()
time.sleep(1)
# 국내부분 선택
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
time.sleep(1)
elem.click()
time.sleep(1)
# 김포국제공항 성택
elem = browser.find_element(By.XPATH,'//i[contains(text(),"김포국제공항")]')
elem.click()
time.sleep(1)

# 도착 선택
elem = browser.find_element(By.XPATH,'//b[text()="도착"]')
time.sleep(1)
elem.click()
time.sleep(1)

# 국내부분 선택
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
time.sleep(1)
elem.click()
time.sleep(1)

# 제주국제공항선택
elem = browser.find_element(By.XPATH,'//i[contains(text(),"제주국제공항")]')
elem.click()
time.sleep(1)

#가는 날 선택
elem = browser.find_element(By.XPATH,'//button[text()="가는 날"]').click()
time.sleep(1)

# 가는 날짜 선택
elem = browser.find_elements(By.XPATH,'//b[text()="14"]')
time.sleep(1)
elem[1].click()
time.sleep(1)
# 오는 날짜 선택
elem = browser.find_elements(By.XPATH,'//b[text()="15"]')
time.sleep(1)
elem[1].click()
time.sleep(1)

# 인워수 선택
elem = browser.find_element(By.XPATH,'//button[text()="성인"]').click()
time.sleep(1)

browser.find_element(By.XPATH,'//button[@class = "searchBox_outer__9n6IB"]').click()
time.sleep(1)

browser.find_element(By.XPATH,'//span[contains(text(),"항공권 검색")]').click()
time.sleep(1)
browser.find_element(By.XPATH,'//span[contains(text(),"항공권 검색")]').click()
time.sleep(1)
# 실제구문 - 1개 가져오기 : find_element
# browser.find_element(By.XPATH,'//i[text()="김포국제공항"]')

# 문자열과 일치할 때 선택방법
# '//i[text()="김포국제공항"]'

# 문자열이 포함되어 있을 때 선택방법
# '//i[contains(text(),"김포국제공항")]'

# id를 가지고 선택방법
# '//i[@id="_next"]'