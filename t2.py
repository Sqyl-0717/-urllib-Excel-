import urllib
import re
from html.parser import HTMLParser
from urllib.request import urlopen

url = 'http://movie.douban.com/review/best/?start='


# 将HTML中的转义字符转换成普通字符
def html_parser(s):

	html_parser = HTMLParser()
	return str(html_parser.unescape(s))


# 获取URL的源代码
def get_html(url, startPage, endPage):
	html = ''
	try:
		for i in range(startPage - 1, endPage):
			url2 = url + str(i * 10)


			req = urllib.request.Request(url2)
			req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE")
			page = urlopen(req)
			print(page.read)
			html = html + str(page.read())
	except:
		print("连接失败")


	return html


def get_movie_review():
	html = get_html(url, 1, 5)

	pattern_title = re.compile(r'<img alt=".*?" title="(.*?)" src=".*?" rel="v:image" />')
	pattern_people = re.compile(r'<a href=".*?" class="name">(.*?)</a>')
	pattern_time = re.compile(r'<span content=".*?" class="main-meta">(.*?)</span>')
	pattern_description = re.compile(r'<div class="short-content">(.*?)&nbsp')
	list_title = re.findall(pattern_title, html)
	list_people = re.findall(pattern_people, html)
	list_time = re.findall(pattern_time, html)
	list_description = re.findall(pattern_description, html)

	print(bytes(list_title[0], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8'))
	print(bytes(list_people[0], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8'))
	print(bytes(list_time[0], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8'))
	print(bytes(list_description[0], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8').replace(" ","").replace("\n","").split('</p>')[-1])

get_movie_review()