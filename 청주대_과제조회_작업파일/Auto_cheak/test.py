from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('headless')
browser = webdriver.Chrome(options=options)

url = "https://hive.cju.ac.kr/common/login/loginpage.do"
browser.get(url)

file = open("User_data.txt", "r", encoding="UTF-8")
User_id, User_pw, HowManyListen = list(map(str, file.read().split()))
file.close()

# 로그인
browser.find_element(By.ID, 'j_username_login').send_keys(User_id)
browser.find_element(By.ID, 'j_password_login').send_keys(User_pw)

browser.find_element(By.XPATH, '//*[@id="FormLogin"]/div/div/div/a').click()
browser.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/div[1]/div[2]/div[1]/div[2]/table/tbody[2]/tr[13]/td[1]/a').click()

try:       
    # WhatisHomework = browser.find_elements(By.CLASS_NAME, 'sche').nextSibling
    # for i in range(len(WhatisHomework)):
    #     print(WhatisHomework[i].text)
    
    When_Homework = browser.find_elements(By.CLASS_NAME, 'item.d_day')

    if bool(When_Homework[0].text) == True: 
        print("과제 있음!")
        for i in range(len(When_Homework)):
            print("과제가 있습니다. " + When_Homework[i].text)
            
    # for i in range(len(WhatisHomework)):
    #     print(len(WhatisHomework))
    #     if (WhatisHomework[i].text != "종료"): 
    #         print("과제가 있습니다!")
    #     else:
    #         print("과제가 없습니다.")
                
except:
    print(" 원래 과제가 없거나 Error" + '\n')  


