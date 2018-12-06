import json
import re
import requests

from sql import maoyan_db_helpr



def get_images(url):
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    return None


def get_page(url):
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    }
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.text
    return None


def get_one_page(html):
    # 解析主演
    actors_pattern=re.compile('<p class="star">(.*?)</p>',re.S)
    actors=re.findall(actors_pattern,html)
    # 解析电影名
    movies_pattern = re.compile(
        '<p class="name"><a href="/films/.*?" title=".*?" data-act="boarditem-click" data-val="{movieId:.*?}">(.*?)</a></p>',
        re.S)
    movies = re.findall(movies_pattern, html)

    # 解析分数
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

    db=maoyan_db_helpr.get_connection()
    cursor=maoyan_db_helpr.get_cursor(db)

    re_list=[]
    for i in range(len(actors)):
        re_dict={}
        re_dict['actor']=actors[i].strip()
        re_dict['movie']=movies[i].strip()
        re_dict['score']=''.join(scores[i])
        re_dict['rate']=rates[i].strip()
        re_dict['time']=times[i].strip()
        re_dict['image']=images[i].strip()

        maoyan_db_helpr.insert_record(db,cursor,re_dict)

        re_list.append(re_dict)

    #关闭数据库
    maoyan_db_helpr.close_connection(db)

    return re_list

def get_all_page():
    result_list=[]
    for i in range(10):
        url='http://maoyan.com/board/4?offset='+ str(i*10)
        result_list.extend(get_one_page(get_page(url)))
    return result_list

def save_images(result_list):
    # 这里的参数就是所获取的所有的字典信息
    for item in result_list:
        cover_url=item['image']
        file_name=cover_url.split('/')[-1].split('@')[0]
        print(cover_url)
        content=get_images(cover_url)

        with open('./xxx/%s'% file_name,'wb')as f:
            f.write(content)

def save_json(result_list):
    json_text=json.dumps(result_list,ensure_ascii=False)
    with open('./maoyan.json','w',encoding='utf-8')as f:
        f.write(json_text)

def read_json(file_name):
    with open(file_name,encoding='utf-8')as f:
        content=json.load(f)
        print(content)


def main():
    # re_list=get_one_page(get_page('http://maoyan.com/board/4'))
    # print(get_all_page())
    url='http://maoyan.com/board/4'
    save_json(get_all_page())
    # read_json('./maoyan.json')



if __name__ == '__main__':
    main()
