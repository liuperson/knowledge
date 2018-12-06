from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:1q2w3e4r5t@127.0.0.1:3306/maoyan_db?charset=utf8", max_overflow=5,encoding='utf-8')
Base = declarative_base()

class MoGuJie(Base):
    __tablename__ = 'mogujie_product'
    id = Column(Integer, primary_key=True, autoincrement=True)    #主键，自增
    tradeitemid = Column(String(512))
    img = Column(String(1024))
    clienturl = Column(String(1024))
    link = Column(String(1024))
    title = Column(String(512))
    orgprice = Column(String(512))
    cfav = Column(String(512))
    price = Column(String(512))
