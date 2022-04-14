#弄清网页结构
#定位需要数据
#保存数据
import urllib
import re
#import HTMLParser
from html.parser import HTMLParser
import excel
from urllib.request import urlopen
import requests
import string

url = 'http://movie.douban.com/review/best/?start=0'
html_parser = HTMLParser()
html = ''
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url,headers = headers)

print(req)
page = urlopen(req,timeout=15)
print(page.read)
html = html + str(page.read())
#asdkawdkjbkjbsjkdab .*?
#pattern_title = re.compile(r'<img alt="(.*?)" title=".*?" src=".*?" rel="v:image" />')
pattern_title = re.compile(r'<img alt=".*?" title="(.*?)" src=".*?" rel="v:image" />')#使用 compile 函数将正则表达式的字符串形式编译为一个 Pattern 对象
pattern_people = re.compile(r'<a href=".*?" class="name">(.*?)</a>')
pattern_time = re.compile(r'<span content=".*?" class="main-meta">(.*?)</span>')
pattern_description = re.compile(r'<div class="short-content">(.*?)&nbsp')

list_title = re.findall(pattern_title, html)   #对pattern对象进行findall操作
list_people = re.findall(pattern_people, html)
list_time = re.findall(pattern_time, html)
list_description = re.findall(pattern_description, html)
#print(list_title[0]) #薛梦丽是一个漂亮的猪猪split('</p>')
#print(bytes(list_title[0], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8').split('</p>')[-1].replace(' ','').replace('\n',''))
print(bytes(list_title[0], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8'))
print(bytes(list_people[0], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8'))
print(bytes(list_time[0], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8'))
print(bytes(list_description[0], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8').replace(" ","").replace("\n","").split('</p>')[-1])