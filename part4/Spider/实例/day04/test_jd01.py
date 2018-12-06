from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
# 高级写法

from urllib.parse import quote
from lxml import etree
import time

chrome_options = webdriver.ChromeOptions()
# 页面启动起来之前还可以做别的
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.set_window_size(1400, 700)
wait = WebDriverWait(browser, 5)


def get_page(page):
    if page == 1:
        url = 'https://www.jd.com'
        browser.get(url)
        # print(browser.page_source)

        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#key')))
        input.clear()
        input.send_keys('机器人')

        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#search button.button')))
        submit.click()

        time.sleep(5)
        print(browser.current_url)

    if page > 1:
        # 填入页码编号
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage input.input-txt')))
        input.clear()
        input.send_keys(page)

        # 点击下一页
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_bottomPage .btn.btn-default')))
        submit.click()

    for i in range(16):
        str_js = 'var step = document.body.scrollHeight / 16; window.scrollTo(0, step * %d)' % (i + 1)
        browser.execute_script(str_js)
        time.sleep(1)

    return browser.page_source


def parse_page(page_source):
    html_etree = etree.HTML(page_source)
    result_list = html_etree.xpath('//div[@id="J_goodsList"]//div[@class="gl-i-wrap"]/div[@class="p-name p-name-type-2"]//em/text()')
    print(result_list)


def main():
    for page in range(2):
        print(page)
        print('-' * 20)
        html = get_page(page + 1)
        parse_page(html)


if __name__ == '__main__':
    main()

