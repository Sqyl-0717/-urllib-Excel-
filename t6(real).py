import urllib
import re
from html.parser import HTMLParser
import excel
from urllib.request import urlopen
import requests
import xlwt

url = 'http://movie.douban.com/review/best/?start='
excel_name = '2.xls' #这一步没啥用，但是删掉会报错
sheet_name = '豆瓣影评' #没啥用，删掉报错
column = ['影片名', '作者', '时间', '影评']

#douban_excel = xlwt.Excel(excel_name, sheet_name) 这方法试了，不行

douban_excel = xlwt.Workbook()  #创建一个对象
#在对象中添加一个sheet1表
write_sheet = xlwt.Workbook.add_sheet(douban_excel,excel_name,sheet_name)

#参考1
#在第二行第三列的单元格插入数据（默认从0开始计数）
#write_sheet.write(1,2,"菜鸟小白的学习分享")
#保存Excel对象为test.xls
#write_book.save(filename_or_stream='test.xls')


# 将HTML中的转义字符转换成普通字符（去掉不可见的字符）
def html_parser(s):
	#print(1)
	html_parser = HTMLParser()
	return str(html_parser.unescape(s))


# 获取URL的源代码
def get_html(url, startPage, endPage):
	html = ''
	try:
		for i in range(startPage - 1, endPage):
			url2 = url + str(i * 20)#观察翻页后url的变化
			req = urllib.request.Request(url2)
			req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE")
			#加入header信息来欺骗，若频繁显示连接失败则被封IP
			page = urlopen(req) #链接动作
			print(page.read) #没啥用，但是显示了能一行一行往外蹦，挺帅的
			html = html + str(page.read()) #存储在变量html中
	except:
		print("连接失败")


	return html


def get_movie_review():
	html = get_html(url, 1, 5) #从第1页到第5页

	pattern_title = re.compile(r'<img alt=".*?" title="(.*?)" src=".*?" rel="v:image" />')#使用 compile 函数将正则表达式的字符串形式编译为一个 Pattern 对象
	pattern_people = re.compile(r'<a href=".*?" class="name">(.*?)</a>')
	pattern_time = re.compile(r'<span content=".*?" class="main-meta">(.*?)</span>')
	pattern_description = re.compile(r'<div class="short-content">(.*?)&nbsp')

	list_title = re.findall(pattern_title, html)   #对pattern对象进行findall操作
	list_people = re.findall(pattern_people, html)
	list_time = re.findall(pattern_time, html)
	list_description = re.findall(pattern_description, html)

	#以下为初步测试所使用：
	#print(bytes(list_title[0], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8'))
	#print(bytes(list_people[0], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8'))
	#print(bytes(list_time[0], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8'))

	#print(bytes(list_description[0], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8').replace(" ","").replace("\n","").split('</p>')[-1])
	#解决乱码问题的操作：bytes(list_description[0], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8')，不加会是/x开头的16进制数，GBK编码
	#replace(" ","").replace("\n","").split('</p>')[-1])去空格，去换行，切分“剧透部分”标签等无用内容

	print('----------写excel开始----------')
	for row in range(0, len(list_title)):
		if row == 0:
			print('----------获取第' + str(row + 1) + '个影评开始----------')
			write_sheet.write(row, 0, column[0])
			write_sheet.write(row, 1, column[1])
			write_sheet.write(row, 2, column[2])
			write_sheet.write(row, 3, column[3])
			write_sheet.write(row + 1, 0, bytes(list_title[row], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8'))
			write_sheet.write(row + 1, 1, bytes(list_people[row], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8'))
			write_sheet.write(row + 1, 2, bytes(list_time[row], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8'))
			write_sheet.write(row + 1, 3, bytes(list_description[row], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8').replace(" ","").replace("\n","").split('</p>')[-1])
			print('影片名：', html_parser(list_title[row]))#显示内容，没啥用，但是挺帅的
			print('作者：', html_parser(list_people[row]))
			print('时间：', html_parser(list_time[row]))
			print('影评：', html_parser(list_description[row]))
			print('----------获取第' + str(row + 1) + '个影评结束----------')
		else:
			print('----------获取第' + str(row + 1) + '个影评开始----------')
			write_sheet.write(row + 1, 0, bytes(list_title[row], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8'))
			write_sheet.write(row + 1, 1, bytes(list_people[row], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8'))
			write_sheet.write(row + 1, 2, bytes(list_time[row], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8'))
			write_sheet.write(row + 1, 3, bytes(list_description[row], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8').replace(" ","").replace("\n","").split('</p>')[-1])
			print('影片名:', html_parser(list_title[row]))
			print('作者:', html_parser(list_people[row]))
			print('时间:', html_parser(list_time[row]))
			print('影评:', html_parser(list_description[row]))
			print('----------获取第' + str(row + 1) + '个影评结束----------')
			print('----------写excel结束,路径：' + excel_name + '----------')

			douban_excel.save(filename_or_stream='test.xls') #此处文件名不能过长，过长会报错

get_movie_review()