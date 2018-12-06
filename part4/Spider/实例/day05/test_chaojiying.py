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

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

# browser = webdriver.Chrome()
browser.set_window_size(1400, 700)
# 显式等待 针对某个节点的等待
wait = WebDriverWait(browser, 10)


def get_page():
    url = 'http://bm.e21cn.com/log/reg.aspx'
    browser.get(url)
    html = browser.page_source
    # 返回的是自己拿到的页面嘛
    return html


# 取浏览器窗口内全图
def get_big_image():
    # 屏幕现在的高度取不完，往下继续
    browser.execute_script('window.scrollTo(0, 300)')
    # 自带函数
    screenshot = browser.get_screenshot_as_png()
    # 自带函数
    screenshot = Image.open(BytesIO(screenshot))
    # 返回拿到的图片（大图）
    return screenshot


# 取验证码坐标位置（左上角和右下角）
def get_position():
    # 高级写法+获取节点+获取验证码图片
    img = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#imgCheckCode')))
    # 获取位置和大小
    loc = img.location
    size = img.size
    print(loc)
    print(size)
    x1 = loc['x']
    # 记住减去滚动高度
    y1 = loc['y'] - 300
    x2 = loc['x'] + size['width']
    y2 = y1 + size['height']
    # 现在的位置就是验证码图片的位置
    return (x1, y1, x2, y2)


# 对页面的解析
def parse_html(html):
    # etree_html = etree.HTML(html)
    screenshot = get_big_image()
    # 全屏的截屏
    screenshot.save('full_screen.png')

    # 利用点来裁剪
    x1, y1, x2, y2 = get_position()
    crop_image = screenshot.crop((x1, y1, x2, y2))
    file_name = 'crop.png'
    crop_image.save(file_name)
    captha_str = main1(file_name)

    # 放在超级鹰里面，得到字节流
    print(captha_str)

    username = 'carmack55'
    password = '123456'
    tel = '18511405897'

    input_username = wait.until(EC.presence_of_element_located
                       ((By.CSS_SELECTOR, 'input#username')))
    input_password1 = wait.until(EC.presence_of_element_located
                       ((By.CSS_SELECTOR, 'input#pwd')))
    input_password2 = wait.until(EC.presence_of_element_located
                                 ((By.CSS_SELECTOR, 'input#pwd_Q')))
    input_tel = wait.until(EC.presence_of_element_located
                                 ((By.CSS_SELECTOR, 'input#tel')))
    input_check = wait.until(EC.presence_of_element_located
                                 ((By.CSS_SELECTOR, 'input#CheckCode')))
    sublime = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#btn_login')))

    input_username.send_keys(username)
    input_password1.send_keys(password)
    input_password2.send_keys(password)
    input_tel.send_keys(tel)
    input_check.send_keys(captha_str)

    # 上面是连续填空进去
    time.sleep(2)
    sublime.click()

def main():
    html = get_page()
    parse_html(html)

if __name__ == '__main__':
    main()

