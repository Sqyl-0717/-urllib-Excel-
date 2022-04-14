from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
import re
import sys
import time
import importlib
importlib.reload(sys)
#sys.setdefaultencoding('utf8')
import base64

def spider(url):
	html = requests.get(url)
	selector = etree.HTML(html.text)
	content_field = selector.xpath('//a[@class="title-link"]/@href')
	for each in content_field:
		#获取文章地址https://movie.douban.com/review/8031102/中的编码号8031102
		num = re.findall("/(\d+)/", each)[0]
		html = requests.get(each)
		selector = etree.HTML(html.text)
		title = selector.xpath('//h1/span/text()')[0]
		rate= selector.xpath('//div[@class="middle"]/header/span/@title')[0]
		movie = selector.xpath('//*[@class="main"]/div[1]/header/a[2]/text()')[0]
		content = selector.xpath('//*[@id="link-report"]/div[1]')[0]
		content = content.xpath('string(.)')
		# content = filter_emoji(content,'emoji')#过滤emoji
		content = base64.b64encode(content)
		print(title)
		time.sleep(1)

if __name__ == '__main__':
	pool = ThreadPool(4)

	jishu = 0
	#time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
	#f = open(time+'_content.txt','a')
	page = []
	for i in range(0,5):
		i = i*10
		newpage = 'https://movie.douban.com/review/best/?start=' + str(i)
		page.append(newpage)

	results = pool.map(spider, page)
	pool.close()
	pool.join()

	yp_time = int(time.time())
	n_date = time.strftime('%Y-%m-%d', time.localtime(yp_time))

