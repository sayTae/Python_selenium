import Cheak5
import User_data_module

def login():
    url = "https://hive.cju.ac.kr/common/login/loginpage.do"
    Cheak5.browser.get(url)
    
    print("로그인 중... (약 2~3초 소요)")
    Cheak5.browser.find_element(Cheak5.By.ID, 'j_username_login').send_keys(User_data_module.User_id)
    Cheak5.browser.find_element(Cheak5.By.ID, 'j_password_login').send_keys(User_data_module.User_pw)
    Cheak5.browser.find_element(Cheak5.By.XPATH, '//*[@id="FormLogin"]/div/div/div/a').click()