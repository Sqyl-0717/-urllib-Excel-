import urllib
import re
#import HTMLParser
from html.parser import HTMLParser
import excel
from urllib.request import urlopen
import requests
import string

url = 'http://movie.douban.com/review/best/?start=1'
html_parser = HTMLParser()
html = ''
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url,headers = headers)

#req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE")

print(req)
page = urlopen(req,timeout=15)
print(page.read)
html = html + str(page.read())
#pattern_title = re.compile(r'<img alt=".*?" title="(.*?)" src=".*?" rel="v:image" />')
#pattern_title = re.compile(r'<a href=".*?" class="name">(.*?)</a>')


pattern_title = re.compile(r'<div class="short-content">(.*?)&nbsp')
list_title = re.findall(pattern_title, html)

#list_title[0] = list_title[0].encode("utf-8").decode('utf-8')
a = bytes(list_title[0], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8').replace(" ","").replace("\n","")
a.translate(str.maketrans('','','<>'))
#print(list_title[0])
#a = bytes(list_title[0], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8')).replace(" ","").replace("\n","")
#print((bytes(list_title[0].replace("\n", ""), 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8')).replace(" ","").replace("\n",""))
print(a)