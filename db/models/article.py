from sqlalchemy import Column, String, Integer
from marshmallow_sqlalchemy import auto_field, SQLAlchemySchema

import time

from db.init import Base, Session

class Article(Base):
    __tablename__ = 'tb_articles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    link = Column(String)
    paragraph = Column(String)
    created_ts = Column(Integer, default=time.time())

    def __init__(self, title, link, paragraph = ''):
        self.title = title
        self.link = link
        self.paragraph = paragraph

class ArticleSchema(SQLAlchemySchema):
    class Meta:
        model = Article
        sqla_session = Session

    id = auto_field()
    title = auto_field()
    link = auto_field()
    paragraph = auto_field()
    created_ts = auto_field()