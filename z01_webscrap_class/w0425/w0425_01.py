import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
url = "https://flight.naver.com/"

# 브라우저 열기
browser = webdriver.Chrome()
browser.maximize_window() # 창 확대
browser.get(url)

time.sleep(3)



# 항권권 사이트에서 국내 여행지 선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[1]/button[1]/b')
elem.click()
time.sleep(2)
elem = browser.find_element(By.CLASS_NAME,'autocomplete_Collapse__tP3pM')
elem.click()
time.sleep(2)

# 김포클릭 - ClASS_NAME 복수개로 가져오기
elem = browser.find_elements(By.CLASS_NAME,'autocomplete_Airport__3_dRP')[2]
elem.click()
time.sleep(2)

#도착 선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[1]/button[2]')
elem.click()
time.sleep(2)
elem = browser.find_element(By.CLASS_NAME,'autocomplete_Collapse__tP3pM')
elem.click()
time.sleep(2)
elem = browser.find_elements(By.CLASS_NAME,'autocomplete_Airport__3_dRP')[1]
elem.click()
time.sleep(2)

# 가는날짜부분 선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[2]/button[1]')
elem.click()
time.sleep(2)

# 가는날짜 선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[1]/button/b')
elem.click()
time.sleep(2)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[2]/button/b')
elem.click()
time.sleep(2)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[3]/button')
elem.click()
time.sleep(2)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[4]/div/div/div[1]/div[1]/button[2]')
elem.click()
time.sleep(2)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/button')
elem.click()
time.sleep(2)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/button')
elem.click()
time.sleep(2)

time.sleep(100)
