import requests
from lxml import etree
import json

from mongodb_helper import *

url='http://www.u17.com/comic/ajax.php?mod=comic_list&act=comic_list_new_fun&a=get_comic_list'
headers = {
    'Referer': 'http://www.u17.com/comic_list/th99_gr99_ca99_ss99_ob0_ac0_as0_wm0_co99_ct99_p1.html?order=2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Host': 'www.u17.com'
}


def parse_html(html):
    e_html = etree.HTML(html)


all_list=[]
def parse_json(html):
    resu=json.loads(html)
    data_list=resu['comic_list']
    re_list=[]
    for item in data_list:
        re_dict={}
        re_dict['comic_id']=item.get('comic_id','')
        re_dict['name']=item.get('name','')
        re_dict['cover']=item.get('cover','')
        re_dict['update_type']=item.get('update_type','')
        re_dict['line2']=item.get('line2','')
        re_list.append(re_dict)
        insert_company(re_dict)
        all_list.extend(re_list)
    return all_list


def get_page(page):
    session=requests.Session()
    post_data = {
        'data[group_id]': 'no',
        'data[theme_id]': 'no',
        'data[is_vip]': 'no',
        'data[accredit]': 'no',
        'data[color]': 'no',
        'data[comic_type]': 'no',
        'data[series_status]': 'no',
        'data[order]':2,
        'data[page_num]': page,
        'data[read_mode]': 'no'
    }
    response=session.post(url,post_data,headers=headers)
    if response.status_code==200:
        return response.text
    return None


def main():
    # page = 1
    # while True:
    #     print(page)
    #     html = get_page(page)
    #     json_result = parse_json(html)
    #     if len(json_result) == 0:
    #         break
    #     print(json_result)
    #     print(len(json_result))
    #     page += 1
    parse_html(get_page(url))

if __name__ == '__main__':
    main()