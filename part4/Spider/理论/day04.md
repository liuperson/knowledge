[TOC]

#####1.selenium

```
from selenium.webdriver import ActionChains
from selenium import webdriver

def f1(xx):
	url='http://www.jd.com'
	xx.get(url)
	
	xx.page_souce
	xx.current_url
	xx.get_cookies()
	
	p1=xx.find_element_by_id('key')
	p1.get_attribute('id')
	
	p2=xx.find_element_by_css_selector('#key')
	p2.location
	
	p3=xx.find_element_by_xpath('//*[@id="key"]')
	p3.id
	
	p4=xx.find_element_by_name('file')
	p4.tag_name
	
	p5=xx.find_element_by_link_text('京东')
	p6=xx.find_element_by_partial_link_text('生鲜')
	
	p5.text
	p6.text

def f2(xx):
	url='http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
	xx.get(url)
	xx.swith_to.frame('iframeResult')
	source = browser.find_element_by_css_selector('#draggable')
	target = browser.find_element_by_css_selector('#droppable')
	
	actions = ActionChains(browser)
	
	actions.drag_and_drop(source, target)
	actions.perform()

def main():
	# 使用chrome浏览器
	browser = webdriver.Chrome()
	# 使用Firefox浏览器
	# browser = webdriver.Firefox()
	# 使用Edge浏览器
	# browser = webdriver.Edge()
	# 使用Phantom浏览器
	# browser = webdriver.PhatomJS()
	# 使用Safari浏览器
	# browser = webdriver.Safari()

	# try:
	# 	f2(browser)
	# finally:
	# 	# 关闭浏览器
	# 	browser.close()
	
	f1(xx)

```