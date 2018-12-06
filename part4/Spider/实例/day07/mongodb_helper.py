import pymongo

client=pymongo.MongoClient()
db=client.manhua

def insert_company(dict):
    db.manhua.insert_one(dict)
