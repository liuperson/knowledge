from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from day03.mogujie_models import MoGuJie

engine = create_engine("mysql+pymysql://root:1q2w3e4r5t@127.0.0.1/maoyan_db?charset=utf8", max_overflow=5)
session_maker = sessionmaker(bind=engine)
session = session_maker()


def save_db(result_list):
    for mogu_dict in result_list:
        mogu=MoGuJie()
        mogu.tradeitemid=mogu_dict['tradeItemId']
        mogu.img=mogu_dict['img']
        mogu.clienturl=mogu_dict['clientUrl']
        mogu.link=mogu_dict['link']
        mogu.title=mogu_dict['title']
        mogu.orgprice=mogu_dict['orgPrice']
        mogu.cfav=mogu_dict['cfav']
        mogu.price=mogu_dict['price']


        session.add(mogu)
        session.commit()
