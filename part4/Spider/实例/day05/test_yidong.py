from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from lxml import etree
from PIL import Image
from io import BytesIO
from day05.chaojiying import main1
import time

# 无头浏览器
# chrome_options.add_argument('--headless')
# 启用Google
chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome(chrome_options=chrome_options)

# browser = webdriver.Chrome()
# 设置屏幕，主要是分辨率
browser.set_window_size(1400, 700)
# 显式等待 针对某个节点的等待,超时就放弃
wait = WebDriverWait(browser, 10)


# 设置获取页面
def get_page():
    url = 'https://login.10086.cn/html/register/register.html'
    browser.get(url)
    html = browser.page_source
    #
    return html

# 取浏览器窗口内全图
def get_big_image():
    browser.execute_script('window.scrollTo(0, 200)')
    screenshot = browser.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(screenshot))
    return screenshot

# 取验证码坐标位置（左上角和右下角）
def get_position():
    img = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#captchaImg')))
    loc = img.location
    size = img.size
    print(loc)
    print(size)
    x1 = loc['x']
    # 记住减去滚动高度
    y1 = loc['y'] - 200
    x2 = loc['x'] + size['width']
    y2 = y1 + size['height']
    return (x1, y1, x2, y2)

def parse_html(html):
    # etree_html = etree.HTML(html)
    screenshot = get_big_image()
    screenshot.save('full_screen1.png')
    x1, y1, x2, y2 = get_position()
    crop_image = screenshot.crop((x1, y1, x2, y2))
    file_name = 'crop1.png'
    crop_image.save(file_name)
    captha_str = main1(file_name)
    
    username = 'carmack55@qq.com'
    password = '1234561qqw2wwe'
    tel = '18511405897'

    print(captha_str)

    input_username = wait.until(EC.presence_of_element_located
                       ((By.CSS_SELECTOR, 'input#loginName')))
    input_password1 = wait.until(EC.presence_of_element_located
                       ((By.CSS_SELECTOR, 'input#newPassword')))
    input_password2 = wait.until(EC.presence_of_element_located
                                 ((By.CSS_SELECTOR, 'input#newPasswordRepeat')))
    # input_tel = wait.until(EC.presence_of_element_located
    #                              ((By.CSS_SELECTOR, 'input#tel')))
    input_check = wait.until(EC.presence_of_element_located
                                 ((By.CSS_SELECTOR, 'input#inputCode')))
    sublime = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#regSub')))
    input_username.send_keys(username)
    input_password1.send_keys(password)
    input_password2.send_keys(password)
    # input_tel.send_keys(tel)
    input_check.send_keys(captha_str)
    time.sleep(2)
    sublime.click()

def main():
	html = get_page()
	parse_html(html)

if __name__ == '__main__':
	main()