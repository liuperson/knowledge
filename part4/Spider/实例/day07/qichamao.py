import requests
from lxml import etree
import json
from mongodb_helper import *


url='https://www.qichamao.com/cert-wall'
headers = {
    'Referer': 'https://www.qichamao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Host': 'www.qichamao.com'
}



def get_first_page():
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    return None

#
def parse_first_page(html):
    first_page=get_first_page()
    e_html=etree.HTML(first_page)
    list_box=e_html.xpath('//div[@class="firmwall_list_box"]')
    result_list=[]
    for item in list_box:
        result_dict = {}
        company_name=item.xpath('.//h2[@class="firmwall_list_tit toe"]/a/text()')[0]
        result_dict['company_name']=company_name
        contact_info=item.xpath('.//li[@class="firmwall_list_citem"]/div[@class="firmwall_list_cinfo"]/text()')[0]
        result_dict['contact_info']=contact_info
        contactor=item.xpath('.//li[@class="firmwall_list_citem firmwall_list_citem2"]/div[@class="firmwall_list_cinfo"]/text()')[0]
        result_dict['contactor']=contactor
        contact_email=item.xpath('//li[@class="firmwall_list_citem"][2]/div[@class="firmwall_list_cinfo"]/text()')
        for xx in contact_email:
            result_dict['contact_email']=xx
            result_list.append(result_dict)

        # del contact_email[0]
        # contact_email=''.join(contact_email)

    return result_list

def parse_json(html):
    result_json=json.loads(html)
    data_list=result_json['dataList']
    re_list=[]
    for item in data_list:
        re_dict={}
        re_dict['company_name']=item.get('CompanyName','')
        re_dict['contactor']=item.get('c_name','')
        re_dict['contact_info']=item.get('c_phone','')
        re_dict['contact_email']=item.get('c_email','')
        insert_company(re_dict)
        re_list.append(re_dict)
    return re_list

#第二页后
def get_page(page):
    session=requests.Session()
    post_data = {'page':page,'pagesize':100}
    response=session.post(url,data=post_data,headers=headers)
    if response.status_code==200:
        return response.text
    return None



def main():
    first_page=get_first_page()
    result_list=parse_first_page(first_page)

    page=2
    while True:
        print(page)
        html=get_page(page)
        json_result=parse_json(html)
        if len(json_result) == 0:
            break
        print(json_result)
        print(len(json_result))
        page += 1

if __name__ == '__main__':
    main()