import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

open_api_key = ''
params = '&pageNo=1&numOfRows=10&startCreateDt=20200121&endCreateDt=20201103'

open_url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=' + open_api_key + params 

res = requests.get(open_url)
soup = BeautifulSoup(res.content, 'html.parser')

data = soup.find_all('item')
# print(soup.items)

print(data)

num_list =[]
exam_list = []
date_list = []
time_list = []

for item in data:
    num = item.find('decidecnt')
    exam = item.find('examcnt')
    date = item.find('statedt')
    time = item.find('statetime')

    print(date, time, num)
  
    num_list.append(num.contents[0]) 
    exam_list.append(exam.contents[0]) 
    date_list.append(date.contents[0]) 
    time_list.append(time.contents[0])

num_new = []
x = [i for i in range(1,len(num_list))]
for i in range(0,len(num_list)-1):
    a = (int(num_list[i])-int(num_list[i+1]))
    print(int(num_list[i]), int(num_list[i+1]), a, date_list[i], time_list[i])
    num_new.append(a)  

x.reverse()

plt.plot(x, num_new)
plt.xlabel("days")
plt.ylabel("confirmed number")
plt.title("daily confirmed number")
# plt.axis([0,310,0, 1000])
plt.show()
