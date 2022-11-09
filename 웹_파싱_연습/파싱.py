import requests
from bs4 import BeautifulSoup

url = "https://hive.cju.ac.kr/usr/classroom/main.do?currentMenuId=&courseApplySeq=3102009&courseActiveSeq=59861"
# https://hive.cju.ac.kr/usr/member/stu/dash/detail.do 청주대 과목 선택
# "https://hive.cju.ac.kr/common/login/loginpage.do;jsessionid=6ED7DAB3CF22AFDD9A1400FC8655A638" 청주대 로그인
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

print(soup.title.get_text()) 