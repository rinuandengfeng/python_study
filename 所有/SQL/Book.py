from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name


[
    User('1', 'Michael'),
    User('2', 'Bob'),
    User('3', 'Adam')
]


class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    # 一对多
    books = relationship('Book')


class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    # '多‘的以访的book表通过外键关联到user表的：
    user_id = Column(String(20), ForeignKey('user.id'))
