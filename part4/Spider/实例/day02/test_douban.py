import json
import requests
import re
from lxml import etree


# 取页面HTML
def get_page(url):
    # url = "https://www.douban.com/group/explore"
    headers =  {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        text = response.content.decode('utf-8')
        return text
    return None


# 获取二进制资源
def get_resource(url):
    # url = "https://www.douban.com/group/explore"
    headers =  {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        text = response.content
        return text
    return None


# 解析一页内容
def parse_one_page(html):
    result_list = []
    html = etree.HTML(html)
    channel_result = html.xpath('//div[@class="channel-item"]')

    for channel in channel_result:
        # 文章标题
        titles = channel.xpath('./div[@class="bd"]/h3/a/text()')[0]
        # print(titles)
        # 喜欢数
        likes = channel.xpath('./div[@class="likes"]/text()[1]')[0]
        # print(likes)
        # 简介
        contents = channel.xpath('./div[@class="bd"]/div[@class="block"]/p/text()')[0]
        # 来自
        groups = channel.xpath('./div[@class="bd"]/div[@class="source"]/span[@class="from"]/a/text()')[0]
        # 上传时间
        time = channel.xpath('./div[@class="bd"]/div[@class="source"]/span[@class="pubtime"]/text()')[0]
        # 来自小组连接
        group_url = channel.xpath('./div[@class="bd"]/div[@class="source"]/span[@class="from"]/a/@href')[0]
        # 图片
        images_url = channel.xpath('./div[@class="bd"]/div[@class="block"]/div[@class="pic"]/div[@class="pic-wrap"]/img/@src')
        # print(images_url)
        if len(images_url) == 0:
            images_url = ''
        else:
            images_url = images_url[0]

        result_dict = {}
        result_dict['title'] = titles
        result_dict['likes'] = likes
        result_dict['content'] = contents
        result_dict['groups'] = groups
        result_dict['time'] = time
        result_dict['group_url'] = group_url
        result_dict['image_url'] = images_url
        result_list.append(result_dict)
    return result_list


def parse_all_page():
    result_list = []
    for i in range(3):
        i = i * 30
        url = "https://www.douban.com/group/explore?start=" + str(i)
        html = get_page(url)
        page_one = parse_one_page(html)
        result_list.extend(page_one)
    return result_list


def save_json(result_list):
    json_text = json.dumps(result_list, ensure_ascii=False)
    with open('./douban.json', 'w', encoding='utf-8') as f:
        f.write(json_text)


def save_images(result_list):
    for result in result_list:
        image_url = result['image_url']
        if len(image_url) != 0:
            image_name = image_url.split('/')[-1]
            print(image_name)
            image = get_resource(image_url)
            with open(f'./images/{image_name}', 'wb') as f:
                f.write(image)


def main():
    # url = "https://www.douban.com/group/explore"
    # html = get_page(url)
    # 解析一页
    # result = parse_one_page(html)
    # print(result)
    # 解析所有页
    # print(result)
    # save_images(result)
    result = parse_all_page()
    save_json(result)


if __name__ == '__main__':
    main()

