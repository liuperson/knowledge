import json
import requests
from lxml import etree


def get_img(image):
    url=image
    headers={"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)" }
    response=requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.content
    return None


def get_page():
    url='https://www.douban.com/group/explore'
    headers={"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)" }
    response=requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.content.decode('utf-8')
    return None


def parse_html(html):
    etree_html = etree.HTML(html)
    # 1.拿所有
    # result=etree_html.xpath('//*')
    # [<Element html at 0x2bd4236a248>, <Element head at 0x2bd4236a348>, <Element meta at 0x2bd4236a2c8>,]
    # 2.拿讨论精选
    # result=etree_html.xpath('//div[@id="content"]/h1//span[@class="head-title"]/text()')
    channel_result=etree_html.xpath('//div[@class="channel-item"]')
    re_list=[]
    for channel in channel_result:
        re_dict={}
        title=channel.xpath('./div[@class="bd"]/h3/a/text()')
        image=channel.xpath('./div[@class="bd"]//div[@class="pic-wrap"]/img/@src')
        content=channel.xpath('./div[@class="bd"]/div[@class="block"]/p/text()')
        source=channel.xpath('./div[@class="bd"]//a/@href')
        source1=channel.xpath('./div[@class="bd"]//a/text()')
        likes=channel.xpath('./div[@class="likes"]/text()')
        re_dict['title']=title[0]
        if image:
            re_dict['image']=image[0]
        else:
            re_dict['image']='https://img1.doubanio.com/view/group_topic/small/public/p150569707.jpg'
        re_dict['content']=content[0]
        re_dict['source']=source[0]
        re_dict['source1']=source1[0]
        re_dict['likes']=likes[0]
        re_list.append(re_dict)
    return re_list


def get_all_page():
    result_list=[]
    for i in range(30):
        result_list.extend(parse_html(get_page()))
    return result_list


def save_image(result_list):
    for item in result_list:
        image=item['image']
        filename=image.split('/')[-1]
        img_url=get_img(image)
        with open('./images/%s'%filename,'wb')as f:
            f.write(img_url)


def save_json(result_list):
    json_text=json.dumps(result_list,ensure_ascii=False)
    with open('./douban.json','w',encoding='utf-8')as f:
        f.write(json_text)


def main():
    save_image(parse_html(get_all_page()))
    save_json(parse_html(get_all_page()))


if __name__ == '__main__':
    main()



