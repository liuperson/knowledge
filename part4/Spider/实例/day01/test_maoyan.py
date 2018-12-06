import requests
import re
import json


# 抓二进制资源
def get_resource(url):
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    return None


# 抓网页
def get_page(url):
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


# 解析页面
def parse_one_page(html):
    result_list = []
    # 主演
    actors_pattern = re.compile('<p class="star">(.*?)</p>', re.S)
    actors = re.findall(actors_pattern, html)
    # 电影
    movies_pattern = re.compile('<p class="name"><a href="/films/.*?" title=".*?" data-act="boarditem-click" data-val="{movieId:.*?}">(.*?)</a></p>', re.S)
    movies = re.findall(movies_pattern, html)
    # 分数
    scores_pattern = re.compile('<p class="score"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i></p>', re.S)
    scores = re.findall(scores_pattern, html)
    # 排名
    rate_pattern = re.compile('<i class="board-index board-index-.*?">(.*?)</i>', re.S)
    rates = re.findall(rate_pattern, html)
    # 上映时间
    time_pattern = re.compile('<p class="releasetime">(.*?)</p>', re.S)
    times = re.findall(time_pattern, html)
    # 图片链接
    images_pattern = re.compile('.*?movieId:.*?>.*?<img.*?<img.*?src="(.*?)"', re.S)
    images = re.findall(images_pattern, html)
    for i in range(len(actors)):
        result_dict = {}
        result_dict['actor'] = actors[i].strip()
        result_dict['movie'] = movies[i].strip()
        result_dict['score'] = ''.join(scores[i])
        result_dict['rate'] = rates[i].strip()
        result_dict['time'] = times[i].strip()
        result_dict['image'] = images[i].strip()
        result_list.append(result_dict)
    return result_list


# 取所有页
def get_all_pages():
    result_list = []
    for page in range(10):
        page = page * 10
        url = 'http://maoyan.com/board/4?offset=' + str(page)
        html = get_page(url)
        result_list.extend(parse_one_page(html))
    return result_list


def write_images_files(result_list):
    for item in result_list:
        cover_url=item['image']
        file_name=cover_url.split('/')[-1].split('@')[0]
        print(cover_url)
        content=get_resource(cover_url)

        with open('./images/%s'% file_name,'wb')as f:
            f.write(content)


def save_json(result_list):
    json_text=json.dumps(result_list,ensure_ascii=False)
    with open('./maoyan.json','w',encoding='utf-8')as f:
        f.write(json_text)


def main():
    # html = get_page('http://maoyan.com/board/4')
    # # print(html)
    # print(parse_one_page(html))
    # write_images_files(get_all_pages())
    print(get_all_pages())
    save_json(get_all_pages())


if __name__ == '__main__':
    main()
