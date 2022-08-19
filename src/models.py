import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__= 'user'

    id = Column (Integer, primary_key = True)
    name = Column (String(120), nullable = False)
    lastname = Column (String(120), nullable = False)
    email = Column (String(50), nullable = False, unique = True)
    password = Column (String(50), nullable = False)


class Follower(Base):
    __tablename__= 'followers'

    follow_id = Column (Integer, ForeignKey('user.user_id'), primary_key = True, nullable=False)
    user_id = Column (Integer, ForeignKey('user.user_id'), primary_key = True, nullable=False)

class Post(Base):
    __tablename__ = 'post'

    post_id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column (Integer, ForeignKey('user.id'), primary_key = True, nullable=False)

class Media(Base):
    __tablename__= 'media'

    media_id = Column (Integer, primary_key = True)
    type = Column (String(120), nullable=False)
    url = Column (String(120), nullable=False)
    post_id = Column (Integer, ForeignKey('post.id'))


class Comment(Base):
    __tablename__ = 'Comment'

    comment_id = Column(Integer, primary_key=True)
    coment_text = Column (String(250), nullable=False)
    author_id = Column (Integer, ForeignKey('user.id'))
    post_id = Column (Integer, ForeignKey('post.id'))


    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e