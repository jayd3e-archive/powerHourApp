from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def initialize_base(engine):
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)


class Song(Base):
    __tablename__ = 'songs'
    #fields
    id = Column(Integer, primary_key=True)
    uri = Column(String)
    genre = Column(String)


class User(Base):
    #table containing all users
    __tablename__ = 'users'
    #fields
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)  # encryption or something should be added. check later.
    email = Column(String)  # in-case we do email authentication
    age = Column(String)
