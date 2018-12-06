from bs4 import BeautifulSoup
import requests
import re


# 取页面HTML
def get_one_page():
	# url = "https://www.xiami.com/chart?spm=a1z1s.3057849.1110925385.2.2sEgfQ"
	# url="http://www.u17.com"
	url="https://sina.cn/?from=web"
	headers =  {
		"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre" 
	}
	response = requests.get(url, headers=headers)
	print(response.status_code)
	if response.status_code == 200:
		text = response.content.decode('utf-8')
		# 或者是gbk gb2312
		return text
	return None


def	parse_with_bs4(html):
	# print(html)
	soup = BeautifulSoup(html, 'lxml')

	# 让页面标签整齐输出
	# print(soup.prettify())

	# 打印的是文字内容
	# print(soup.title.string)

	# 取head标签
	# print(soup.head)

	# 第一个p标签
	# print(soup.p)

	# p标签的名字
	# print(soup.p.name)

	# 取不到就没有img
	# print(soup.img.attrs["src"])

	# print(soup.img.attrs)
	# print(soup.img.attrs['src'])
	# print(soup.img['src'])
	# print(soup.p.string)
	
	# l = soup.select('.ct_t_01 a')
	# for item in l:
	# 	print(item.string)
	# 	print(item['href'])
	# print(len(l))
	# item = soup.select('#syncad_1 p')[0]
	# # print(item)
	# print(item.contents)
	# print(len(item.contents))
	# item = soup.select('.b_time')[0].string
	# print(item)

	# 嵌套
	# print(soup.head.title.string)

	# 关联选择
	# <p class="p1"></p>
	# <p></p>
	# print(soup.p.contents)
	# print(soup.p.parent)
	# print(list(soup.a.parents)[0].attrs['class'])
	# print(soup.prettify())
	# print(soup.ul.li)


def main():
	html = get_one_page()
	html='<ul><li>aaa<li></ul><ul><li>bbb</li>mmm<li>ccc</li></ul>'
	parse_with_bs4(html)


if __name__ == '__main__':
	main()
