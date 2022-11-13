from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome("./chromedriver.exe")

Arrys = {"JAVA스크립트":[3102009,59861], "디지털보안의이해":[59869,3102335], "파이썬프로그래밍":[59871,3102425],
 "빅데이터통계학개론":[59877,3102599], "인공지능이해":[59885,3102781], "논리적글쓰기":[60951,3109529],
 "English2":[61309,3120293], "수학2":[61991,3134791], "컴퓨팅사고":[61993,3134877]
 }

Apply = 3102009
Active = 59861

url = f"https://hive.cju.ac.kr/usr/classroom/main.do?currentMenuId=&courseApplySeq={Apply}&courseActiveSeq={Active}"
browser.get(url)

# 2. 값 출력
whenWork = browser.find_element(By.CLASS_NAME, 'sche')
print(whenWork.text)




# https://hive.cju.ac.kr/usr/classroom/main.do?currentMenuId=&courseApplySeq=3102009&courseActiveSeq=59861