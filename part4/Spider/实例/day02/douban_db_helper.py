import json
import pymysql


def read_json(file_name):
    with open(file_name,'r',encoding='utf-8')as f:
        content=json.load(f)
        return content

result=read_json('./douban.json')


def main():
    host='127.0.0.1'
    port=3306
    user='root'
    password='1q2w3e4r5t'
    database='blog'
    db=pymysql.connect(host,user,password,database,charset='utf8',port=port)
    cursor=db.cursor()

    for item in result:
        sql="insert into test2 (title,likes,content,groups,time,group_url,image_url) values ('%s','%s','%s','%s','%s','%s','%s')"% (item['title'],item['likes'],item['content'],item['groups'],item['time'],item['group_url'],item['image_url'])
        print(sql)
        cursor.execute(sql)
        db.commit()

if __name__ == '__main__':
    main()
