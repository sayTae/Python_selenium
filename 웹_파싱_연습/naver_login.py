from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome("./chromedriver.exe")
url = "https://hive.cju.ac.kr/common/login/loginpage.do"
url2 = "https://naver.com"
browser.get(url2)

# 1. 네이버 접속
elem = browser.find_element(By.CLASS_NAME,'link_login')
elem.click()

# 2. 로그인
browser.find_element(By.ID, 'id').send_keys("mattam1129")
time.sleep(1)
browser.find_element(By.ID, 'pw').send_keys("dksxodud1324~")

time.sleep(1)

# 3. 로그인 버튼 클릭
browser.find_element(By.ID, 'log.login').click()


while(True):
    pass