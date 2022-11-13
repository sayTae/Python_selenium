from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('headless')
browser = webdriver.Chrome(options=options)

url = "https://hive.cju.ac.kr/common/login/loginpage.do"
browser.get(url)

file = open("싹다_연습\GUI로_제작\User_data.txt", "r", encoding="UTF-8")
User_id, User_pw, HowManyListen = list(map(str, file.read().split()))
file.close()

# 로그인
print("로그인 중... (약 2~3초 소요)")
browser.find_element(By.ID, 'j_username_login').send_keys(User_id)
browser.find_element(By.ID, 'j_password_login').send_keys(User_pw)

browser.find_element(By.XPATH, '//*[@id="FormLogin"]/div/div/div/a').click()

# 수강 과목 리스트 생성
topic_list = []
for i in range(1,18,2):
    topic_xPath = f'//*[@id="content"]/div[3]/div/div[1]/div[2]/div[1]/div[2]/table/tbody[2]/tr[{i}]/td[1]/a'
    
    a = browser.find_element(By.XPATH, topic_xPath)
    topic_list.append("");
    topic_list.append(a.text);

# 수강 과목 과제 cheak 함수
def period(n):
    class_name_xPath = f'//*[@id="content"]/div[3]/div/div[1]/div[2]/div[1]/div[2]/table/tbody[2]/tr[{n}]/td[1]/a'
    browser.find_element(By.XPATH, class_name_xPath).click()
    
    try:          
        When_Homework = browser.find_elements(By.CLASS_NAME, 'item.d_day')

        if bool(When_Homework[0].text) == True: 
            print('-' *60, "\n")
            print("<" + topic_list[n] + "> 과제 있음!")
            
            for i in range(len(When_Homework)):
                print("<" + topic_list[n] + "> 과제가 있습니다. " + When_Homework[i].text + "\n")
                   
    except:
        print('-' *60)
        print("<" + topic_list[n] + "> 과제가 없거나, 원래 이 강의는 과제가 없습니다.")
         
    browser.back(); time.sleep(0.2);
    
# cheak 반복 
for i in range(1, int(HowManyListen) *2, 2):
    period(i)


exit();