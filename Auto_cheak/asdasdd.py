from selenium import webdriver  
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument('headless')
browser = webdriver.Chrome(options=options)

url = "https://hive.cju.ac.kr/usr/classroom/main.do?currentMenuId=&courseApplySeq=3134791&courseActiveSeq=61991"
browser.get(url)

file = open("User_data.txt", "r", encoding="UTF-8")
User_id, User_pw, HowManyListen = list(map(str, file.read().split()))
file.close()

# 로그인
print("로그인 중... (약 2~3초 소요)")
browser.find_element(By.ID, 'j_username_login').send_keys(User_id)
browser.find_element(By.ID, 'j_password_login').send_keys(User_pw)
browser.find_element(By.XPATH, '//*[@id="FormLogin"]/div/div/div/a').click()

User_name = browser.find_element(By.XPATH, '//*[@id="header"]/div[1]/div/div/ul/li[1]/span')
print(User_name.text + "님, 로그인이 정상적으로 확인되었습니다. \n\n과제 조회를 시작합니다.")

class_name_xPath = f'//*[@id="content"]/div[3]/div/div[1]/div[2]/div[1]/div[2]/table/tbody[2]/tr[15]/td[1]/a'
browser.find_element(By.XPATH, class_name_xPath).click()

time.sleep(2)
browser.find_element(By.CLASS_NAME, 'item.join').click()
anal_title = browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/table/tbody/tr[2]/td')
anal_result = browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/table/tbody/tr[3]/td')
print("과제 제목: " + anal_title.text + "\n" + "과제 내용: " + anal_result.text)
browser.back();