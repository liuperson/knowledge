from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
# 高级写法

from urllib.parse import quote
from lxml import etree
import time

# 服务器起前做其他操作
chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome(chrome_options=chrome_options)

# 设置宽高
browser.set_window_size(1400, 700)
# 时间
wait = WebDriverWait(browser, 5)


def get_page(page):
    # 第一页
    if page == 1:
        url = 'https://www.jd.com'
        # 将url给browser
        browser.get(url)
        # print(browser.page_source)打印属性

                # 对象.方法(EC.方法(选目标，选择的目标))
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#key')))
        # 对象.清除方法
        input.clear()
        # 对象赋值
        input.send_keys('机器人')

                # 对象.方法(EC.方法(选目标，选择的目标))
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#search button.button')))
                # 点击方法
        submit.click()

        # 时间间隔5，给网页加载时间
        time.sleep(5)
        # 打印当前的网址，就是跳转后网址
        print(browser.current_url)

    # 后面页
    if page > 1:
        # 依然是选中目标
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage input.input-txt')))
        input.clear()
        input.send_keys(page)

        # 点击事件
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_bottomPage .btn.btn-default')))
        submit.click()

    # 无论是否第一页，这里都要循环浏览，网页自动进行下降
    for i in range(16):
      str_js = 'var step = document.body.scrollHeight / 16; window.scrollTo(0, step * %d)' % (i + 1)
      browser.execute_script(str_js)
      # 每次循环间隔1秒
      time.sleep(1)

    # 返回页面内容，是循环后的内容
    return browser.page_source


    # 将循环后得到的页面丢过来进行解析
def parse_page(page_source):
    # etree方法
    html_etree = etree.HTML(page_source)
    # xpath方法进行匹配
    result_list = html_etree.xpath('//div[@id="J_goodsList"]//div[@class="gl-i-wrap"]/div[@class="p-name p-name-type-2"]//em/text()')
    # 打印匹配的结果
    print(result_list)


def main():
    # 根据自己想要多少页，做循环
    for page in range(2):
        # 打印页数
        print(page)
        print('-' * 20)
        # 串参解析
        html = get_page(page + 1)
        parse_page(html)

if __name__ == '__main__':
    main()

