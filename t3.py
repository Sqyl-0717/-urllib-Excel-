import urllib
import re
import HTMLParser
import excel

url = 'http://movie.douban.com/review/best/?start='
excel_name = './excel/douban_hot_review.xls'
sheet_name = '豆瓣影评'
column = ['标题', '作者', '影片', '影评']

douban_excel = excel.Excel(excel_name, sheet_name)


# 将HTML中的转义字符转换成普通字符
def html_parser(s):
	html_parser = HTMLParser.HTMLParser()
	return str(html_parser.unescape(s))


# 获取URL的源代码
def get_html(url, startPage, endPage):
	html = ''
	for i in range(startPage - 1, endPage):
		url2 = url + str(i * 10)
		try:
			page = urllib.urlopen(url2)
			html = html + page.read()
		except:
			print(url2 + '，网络链接异常')

	return html


def get_movie_review():
	html = get_html(url, 1, 5)

	pattern_title = re.compile(r'<a class="" title="(.+)" href')
	pattern_people = re.compile(r'<a.+people.+">(.+)</a>')
	pattern_subject = re.compile(r'<a.+subject.+" title="(.+)">')
	pattern_description = re.compile('<span class="">([^(][\s\S]+?)</span>')

	list_title = re.findall(pattern_title, html)
	list_people = re.findall(pattern_people, html)
	list_subject = re.findall(pattern_subject, html)
	list_description = re.findall(pattern_description, html)

	print('----------写excel开始----------')
	for row in range(0, len(list_title)):
		if row == 0:
			print('----------获取第' + str(row + 1) + '个影评开始----------')
			douban_excel.write(row, 0, column[0])
			douban_excel.write(row, 1, column[1])
			douban_excel.write(row, 2, column[2])
			douban_excel.write(row, 3, column[3])
			douban_excel.write(row + 1, 0, html_parser(list_title[row]))
			douban_excel.write(row + 1, 1, html_parser(list_people[row]))
			douban_excel.write(row + 1, 2, html_parser(list_subject[row]))
			douban_excel.write(row + 1, 3, html_parser(list_description[row]))
			print('标题：', html_parser(list_title[row]))
			print('作者：', html_parser(list_people[row]))
			print('影片：', html_parser(list_subject[row]))
			print('影评：', html_parser(list_description[row]))
			print('----------获取第' + str(row + 1) + '个影评结束----------')
		else:
			print('----------获取第' + str(row + 1) + '个影评开始----------')
			douban_excel.write(row + 1, 0, html_parser(list_title[row]))
			douban_excel.write(row + 1, 1, html_parser(list_people[row]))
			douban_excel.write(row + 1, 2, html_parser(list_subject[row]))
			douban_excel.write(row + 1, 3, html_parser(list_description[row]))
			print('标题:', html_parser(list_title[row]))
			print('作者:', html_parser(list_people[row]))
			print('影片:', html_parser(list_subject[row]))
			print('影评:', html_parser(list_description[row])
			print('----------获取第' + str(row + 1) + '个影评结束----------')
	print('----------写excel结束,路径：' + excel_name + '----------')

	douban_excel.save()


get_movie_review()