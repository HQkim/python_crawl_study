from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless")

# webdriver 설정(Chrome, Firefox 등) - Headless 모드
browser = webdriver.Chrome('C:/Users/HK Kim/develop/python_crawl/webdriver/chrome/chromedriver.exe', options=chrome_options)

# webdriver 설정(Chrome, Firefox 등) - 일반 모드
# browser = webdriver.Chrome('C:/Users/HK Kim/develop/python_crawl/webdriver/chrome/chromedriver.exe')

# 크롬 브라우저 내부 대기
browser.implicitly_wait(5)

# 브라우저 사이즈
browser.set_window_size(1920, 1280) # maximize_window(), minimize_window()

# 페이지 이동
browser.get('https://coronaboard.kr/')

# bs4 초기화
soup = BeautifulSoup(browser.page_source, 'html.parser')

# 필요한 데이터 검색
title=soup.find('title')

confirmed= soup.find_all('p', class_='confirmed')
# confirmed_diff= soup.find_all('p', 'death red number')

# 필요한 데이터 출력 및 저장
# 출력
for t in confirmed:
    print(t.string)

# 저장
now = datetime.now()
f= open("C:/Users/HK Kim/Desktop/corona_s.txt",'a')
f.write("%s분 %s월 %s일 %s시 %s분" %(now.year, now.month, now.day, now.hour, now.minute))
f.write("\n")
f.write(title.get_text())
f.write("\n")
for t in confirmed:
    f.write(str(t.string))
    f.write("\n")
f.write("\n")
f.close()