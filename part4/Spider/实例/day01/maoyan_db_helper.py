import pymysql

# 获取数据库连接
def get_connection():
    host = '127.0.0.1'
    port = 3306
    user = 'root'
    password = '1q2w3e4r5t'
    database = 'maoyan_db'
    db = pymysql.connect(host, user, password, database, charset='utf8', port=port)
    return db


def get_cursor(db):
    cursor = db.cursor()
    return cursor


#插入数据
def insert_record(db,cursor,item):
    sql="insert into maoyan (actor,movie,score,rate,htime,image) values ('%s','%s','%s','%s','%s','%s')"\
        %(item['actor'],item['movie'],item['score'],item['rate'],item['time'],item['image'])
    print(sql)
    cursor.execute(sql)
    db.commit()


#关闭数据库连接
def close_connection(db):
    db.close()



