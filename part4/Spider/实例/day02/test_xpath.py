import json

import requests
import re
from lxml import etree


# 取页面HTML
def get_one_page():
	url = "https://www.douban.com/group/explore"
	headers =  {
		"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)" 
	}
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		text = response.content.decode('utf-8')
		return text
	return None


# 解析页面
def parse_with_xpath(html):
	etree_html = etree.HTML(html)
	print(etree_html)

	# 匹配所有节点 //*
	# result = etree_html.xpath('//*')
	# print(result)
	# print(len(result))

	# 匹配所有子节点 //a     文本获取：text()
	# result = etree_html.xpath('//a/text()')
	# print(result)

	# 查找元素子节点 /
	# result = etree_html.xpath('//div/p/text()')
	# print(result)

	# 查找元素所有子孙节点 //
	# result = etree_html.xpath('//div[@class="channel-item"] | //span[@class="pubtime"]/../span/a/text()')
	# result = etree_html.xpath('//div[@class="channel-item"]')
	# 这是节点对象，所以可以继续
	# result.xpath('')
	# print(result)

	# def write(result):
	# 	json_text=json.dumps(result,ensure_ascii=False)
	# 	with open('./'):
	# 		pass

	# 父节点 ..
	# result = etree_html.xpath('//span[@class="pubtime"]/../span/a/text()')
	# 往上走一层，然后找a标签的text()
	# print(result)

	# 属性匹配 [@class="xxx"]
	# 文本匹配 text() 获取所有文本//text()
	# 大量的article里面的所有的文字，和单/有区别
	# result = etree_html.xpath('//div[@class="article"]//text()')
	# print(result)

	# 属性获取 @href
	# result = etree_html.xpath('//div[@class="article"]/div/div/@class')[0]
	# 获取的是属性的值
	# # result = etree_html.xpath('//div[@class="bd"]/h3/a/@href')
	# print(result)

	# 属性多值匹配 contains(@class 'xx')
	# result = etree_html.xpath('//div[contains(@class, "grid-16-8")]//div[@class="likes"]/text()[1]')
	# 找到标签，然后是它下面所有的寻找class是likes的div下面的text(),第一个，语法不一样
	# print(result)

	# 多属性匹配 or, and, mod, //book | //cd, + - * div = != < > <= >=
	# result = etree_html.xpath('//span[@class="pubtime" and contains(text(), "12:")]/text()')
	# 标签是pubtime,然后的话它的内容文本包含12，获取它的文本
	# print(result)

	# 按序选择 [1] [last()] [poistion() < 3] [last() -2]
	# 节点轴
	# //li/ancestor::*  所有祖先节点
	# //li/ancestor::div div这个祖先节点
	# //li/attribute::* attribute轴，获取li节点所有属性值
	# //li/child::a[@href="link1.html"]  child轴，获取直接子节点
	# //li/descendant::span 获取所有span类型的子孙节点	
	# //li/following::* 选取文档中当前节点的结束标记之后的所有节点
	# //li/following-sibling::*     选取当前节点之后的所用同级节点

	# result = etree_html.xpath('//div[@class="channel-item"][1]/following-sibling::*')
	# print(result)
	# print(len(result))

	# result = etree_html.xpath('//div[contains(@class, "channel-group-rec")]//div[@class="title"]/following::*[1]/text()')
	# print(result)


def main():
	html = get_one_page()
	parse_with_xpath(html)


if __name__ == '__main__':
	main()