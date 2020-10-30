import requests
from bs4 import BeautifulSoup

# 1) reqeusts 라이브러리를 활용한 HTML 페이지 요청 
# 1-1) res 객체에 HTML 데이터가 저장되고, res.content로 데이터를 추출할 수 있음
res = requests.get('https://www.space.com/news')

# 2) HTML 페이지 파싱 BeautifulSoup(HTML데이터, 파싱방법)
# 2-1) BeautifulSoup 파싱방법
soup = BeautifulSoup(res.content, 'html.parser')

# 3) 필요한 데이터 검색
title=soup.find('title')
article_name = soup.find_all('h3', class_='article-name')
# confirmed_diff= soup.find_all('p', 'death red number')
# print(article_name)

# 4) 필요한 데이터 출력 및 저장
# 4-1)프린트
print(title.get_text())
for t in article_name:
    print(t.text)


# 4_2)외부파일에 출력 및 저장
f= open("C:/Users/Hyunkyu/Desktop/spacenews.txt",'w', -1, "utf-8") # 'w'뒤에 -1(버퍼라는데 뭔지모름)랑 utf-8 안해주면 에러남. http://blog.naver.com/PostView.nhn?blogId=rjs5730&logNo=220980957605&parentCategoryNo=&categoryNo=&viewDate=&isShowPopularPosts=false&from=postView
f.write(title.get_text())
f.write("\n\n")
i=1
for t in article_name:
    f.write(str(i))
    f.write(" ")
    f.write(t.text) 
    f.write("\n")
    i+=1

f.close()
