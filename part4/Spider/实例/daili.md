[TOC]

##### 1.xx

```
def main():
    page = 1
    proxy = None

    while (True):
        url = 'https://list.mogujie.com/search?	callback=jQuery21108307139015410421_1543376477667&_version' \
                '=8193&ratio=3%3A4&cKey=15&page=' + str(page) + '&sort=pop&ad=0&fcid=50330&action=shoes&acm=' \
                '3.mce.1_10_1jxc6.128038.0.5fV4draFaldTp.pos_4-m_464807-sd_119&ptp=1.n5T00.0.0.4pF9qC5C&_=1543376477669'

        html=''
        try:
            html = get_one_page(url, proxies)
        except Exception as e:
            html=''

        if '(' not in html:
            print('.......in error.......')
            # t = random.randint(1, 3)
            # time.sleep(t)
            proxy=proxies.get_proxies()
            print(proxy)
            continue
        result_list = parse_page(html)

        if result_list is None:
            break
        print(page, len(result_list))
        sqlalchemy_helper.save_db(result_list)
        write_json(result_list)
        page += 1    
```

#####2.dd


```
def get_one_page(url,proxies):
    agent = get_random_agent()
    if proxies is None:
        response = requests.get(url, headers=headers)
    else:
        response = requests.get(url, headers=headers,proxies=proxies)

    if response.status_code == 200:
        text = response.content.decode('utf-8')
        return text
    return None
    # 这里用到的sqlalchemy_helper
    #1.出随机时间
    #2.出随机user-agent
    #3.sqlalchemy里面出随机ip，这里代理池
    #4.超级鹰
    
```