import requests
from bs4 import BeautifulSoup

# 1) reqeusts 라이브러리를 활용한 HTML 페이지 요청 
# 1-1) res 객체에 HTML 데이터가 저장되고, res.content로 데이터를 추출할 수 있음
res = requests.get('https://coronaboard.kr')


# 2) HTML 페이지 파싱 BeautifulSoup(HTML데이터, 파싱방법)
# 2-1) BeautifulSoup 파싱방법
soup = BeautifulSoup(res.content, 'html.parser')

# 3) 필요한 데이터 검색
title=soup.find('title')
confirmed_n = soup.find_all('p', class_='confirmed number')
# confirmed_diff= soup.find_all('p', 'death red number')

# 4) 필요한 데이터 출력 및 저장
# 출력
for t in confirmed_n:
    print(t.string)

# 저장
f= open("C:/Users/HK Kim/Desktop/corona_b.txt",'w')
f.write(title.get_text())
f.write("\n")
for t in confirmed_n:
    f.write(str(t.string))
    f.write("\n")

f.close()
