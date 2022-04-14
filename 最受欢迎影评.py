
import requests
import bs4
from bs4 import BeautifulSoup
kv={'user-agent':'Mozilla/5.0'}
r= requests.get("https://movie.douban.com/review/best/",headers=kv)
r.encoding=r.apparent_encoding
#print (r.status_code)
#print (r.request.headers)
soup=BeautifulSoup(r.text,"html.parser")
print("用户名；星级；评价时间；详细评价")
for house in (soup.find_all('div',class_='main review-item')):
	if isinstance(house, bs4.element.Tag):
		n = house.find('a',class_='subject-img').find_all('img')
		n = str(n)
		#print(n)
		nam = n.split('title=')[-1]
		name = nam.replace("/>]","")
		username=house.find('header',class_='main-hd').find('a',class_='name').string
		leave=house.find('header', class_='main-hd').find_all('span')[0].get('title')
		time=house.find('header', class_='main-hd').find('span',class_='main-meta').string
		evaluate=house.find('div',class_='main-bd').find('div',class_='short-content').contents[0]
		e1=house.find('div',class_='main-bd').find('div',class_='short-content').contents[2]
		evaluate=evaluate+e1
		print ("(%s,%s,%s,%s,%s)" % (name,username,leave,time,evaluate.strip()))
